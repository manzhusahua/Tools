"""
VM script for alignment using SpeechOptimizedParallelRunStep
Copyright (c) Microsoft Corporation
"""
import csv
import os
import pandas as pd
import shutil
import sys

import wave

from os.path import dirname, realpath, sep, pardir
from pathlib import Path

sys.path.append(dirname(__file__))
sys.path.append(dirname(realpath(__file__)))
sys.path.append(dirname(realpath(__file__)) + sep + pardir)
import util.transcription.dataprocessing as comman_dataprocessing

from base_step.chunkinputbasestep import ChunkInputBaseStep
from cascades.data.block import (
    BinaryChunkLister,
    BinaryChunkDeserializer,
    DataPipe,
)
from util.step_stats_info import StepStatsInfo


class ChunkData2TTSFormat(ChunkInputBaseStep):
    def __init__(self) -> None:
        super().__init__(reserve_source_chunks=False)

    def init(self, snapshot_dir="", resource_dir_dict={}, arg_list=[]):
        pass

    def copy_chunk_data(
        self,
        chunk_name,
        from_dir,
        to_dir,
        file_type_list=[],
        override=True,
        delete_after_copy=False,
    ):
        # "Finalize and relocate data step 6"
        if not self.is_copy_chunk_data:
            return

        self.logger.info(f"Start copy chunk {chunk_name} data to output folder {to_dir}.")
        to_dir = Path(to_dir)
        chunk_folder = to_dir / chunk_name
        os.makedirs(chunk_folder, exist_ok=True)

        source_metadata_file = os.path.join(from_dir, chunk_name, "metadata.csv")
        target_metadata_file = os.path.join(chunk_folder, "metadata.csv")
        shutil.copyfile(source_metadata_file, target_metadata_file)

        source_zipwave_file = os.path.join(from_dir, chunk_name, "waves.zip")
        target_zipwave_file = os.path.join(chunk_folder, "waves.zip")
        shutil.copyfile(source_zipwave_file, target_zipwave_file)

        if delete_after_copy:
            shutil.rmtree(from_dir)
        self.logger.info(f"Finished copy chunk {chunk_name} data to output folder {chunk_folder}.")

    def get_audio_length(self, filename):
        # wave module only support str filename
        if isinstance(filename, Path):
            filename = str(filename)
        with wave.open(filename) as f:
            return f.getnframes() / f.getframerate()

    def ConverChunk2TTSDataFormat(self, chunk_dir, chunk_name, output_dir, cur_stats):
        try:
            chunk_json = os.path.join(chunk_dir, chunk_name + ".json")
            blocks = [
                BinaryChunkLister(chunk_json, types_to_load=["audio", "info","transcription"]),
                BinaryChunkDeserializer(),
            ]

            valid_blocks = [block for block in blocks if block is not None]
            chunk_iter = DataPipe(*valid_blocks)

            file_count = 0

            data_frame = None

            def textcheck(text):
                if text == "":
                    return False
                if "<unk>" in text.lower():
                    return False
                return True

            wave_file_list = []
            for utt in chunk_iter:
                try:
                    wav_file_name = utt["info"]["filename"]
                    cur_stats.add_original_files(1)
                    if wav_file_name[-4:].lower() == ".wav":
                        wav_file_name = wav_file_name[:-4]
                    wave_data = utt["audio"]
                    wav_file_path = os.path.join(output_dir, f"{wav_file_name}{'.wav'}")
                    with open(wav_file_path, "wb") as f:
                        f.write(wave_data)
                    if not os.path.isfile(wav_file_path):
                        self.logger.info(f"Failed to write {wav_file_path}")
                        cur_stats.add_failed_files(1)
                        continue

                    # segmentation = utt["info"]["segmentation"]
                    segmentation = utt["transcription"]
                    row_values1 = {
                        "wav": [wav_file_name+".wav"],
                        # "text": [text],
                        "text": [segmentation],
                        "textless": ["false"],
                        "human_voice": ["true"],
                        "multispeaker_detect_score": ["-9999"],
                    }
                    # if not isinstance(segmentation, list):
                    #     print(3)
                    #     cur_stats.add_failed_files(1)
                    #     continue

                    if data_frame is None:
                        data_frame = pd.DataFrame(row_values1)
                    else:
                        newdata = pd.DataFrame(row_values1)
                        data_frame = pd.concat([data_frame, newdata], axis=0, ignore_index=True)
                    wave_file_list.append(wav_file_path)
                    cur_stats.add_succeeded_files(1)
                    cur_stats.add_succeeded_duration(self.get_audio_length(wav_file_path))

                    file_count += 1
                except Exception as e:
                    print(f"When processing {wav_file_name} faced error {e}")
                    cur_stats.add_failed_files(1)
                    continue

            # if file_count == 0:
            #     print("No valid file found in the chunk")
            #     return False

            meta_file = os.path.join(output_dir, "metadata.csv")
            data_frame.to_csv(
                meta_file, sep="|", encoding="utf-8", index=False, quoting=csv.QUOTE_NONE
            )

            zip_wave_file = os.path.join(output_dir, "waves.zip")
            comman_dataprocessing.zip_file_list(
                wave_file_list, zip_wave_file, prefix_removal=output_dir
            )

            return True
        except Exception as e:
            print(f"When processing chunk {chunk_name} faced error {e}.")
            return False

    def process_a_chunk(self, chunk_name, chunk_dir, output_dir):
        """
        Performs alignment for a single chunk
        Args:
            chunk_name (str): The chunk name
            chunk_dir (str): directory path for the chunk
            output_dir (str): output directory path for the alignment chunk file
        """

        self.logger.info(
            "Start NTTS data processing for chunk %s in directory %s" % (chunk_name, chunk_dir)
        )

        os.makedirs(output_dir, exist_ok=True)

        chunk_NTTS_folder = os.path.join(output_dir, chunk_name)
        if os.path.exists(chunk_NTTS_folder):
            shutil.rmtree(chunk_NTTS_folder)
        os.makedirs(chunk_NTTS_folder, exist_ok=True)

        self.is_copy_chunk_data = True
        cur_stats = StepStatsInfo()
        if not self.ConverChunk2TTSDataFormat(chunk_dir, chunk_name, chunk_NTTS_folder, cur_stats):
            self.is_copy_chunk_data = False
        return cur_stats


# This is the required functions for AML PRS step. They will be called by PRS system code
CHUNK_STEP = None


def init():
    global CHUNK_STEP
    CHUNK_STEP = ChunkData2TTSFormat()
    CHUNK_STEP.prs_step_init()


def run(mini_batch):
    return CHUNK_STEP.prs_step_run(mini_batch)


# End of the required functions for AML PRS step


# This function can contain main func so we can quickly local dev and debug this file
if __name__ == "__main__":
    from util.logger_util import LoggerUtil

    LoggerUtil.setup_logger()

    dataset_path = r"./test/test_data/sample_chunks/zn-CN-chunk/chunk_files"
    chunk_name_list = [
        "chunk_00122597-34d2-11ee-a984-002248b798ca",
    ]

    temp_output_path = r"./test/test_data/sample_chunks/zn-CN-chunk/temp"
    if os.path.exists(temp_output_path):
        shutil.rmtree(temp_output_path)
    os.makedirs(temp_output_path, exist_ok=True)
    final_output_path = r"./test/test_data/sample_chunks/zn-CN-chunk/result"
    if os.path.exists(final_output_path):
        shutil.rmtree(final_output_path)
    os.makedirs(final_output_path, exist_ok=True)

    chunkdata2ttsformat_processing = ChunkData2TTSFormat()
    chunkdata2ttsformat_processing.init()

    for chunk_name in chunk_name_list:
        chunkdata2ttsformat_processing.process_a_chunk(chunk_name, dataset_path, temp_output_path)
        chunkdata2ttsformat_processing.copy_chunk_data(
            chunk_name, temp_output_path, final_output_path, delete_after_copy=True
        )

    # if os.path.exists(temp_output_path):
    #     shutil.rmtree(temp_output_path)
    # if os.path.exists(final_output_path):
    #     shutil.rmtree(final_output_path)

    print("Done")
