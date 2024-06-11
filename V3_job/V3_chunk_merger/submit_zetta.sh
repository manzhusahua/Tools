#!/bin/bash


workspace_name="zetta-prod-ws01-wus2"
compute_target="ZettA-AML-Test"

inputdir="/datablob/TTS_ChunkData/SR_Chunk/v3/SR_Chunk_temp/ko-KR_TTS_20240305/raw_data"
# outputdir="/modelblob/v-zhazhai/test/merger_chunk"
command="python check_sppech_length.py "$inputdir

experiment_name="check_sppech_length"
display_name="ko-KR_TTS_20240305"

"C:\Users\v-zhazhai\Toosl\miniconda3\envs\use\python.exe" -u submit/zetta_submit.py \
  --workspace-name "${workspace_name}" \
  --compute-target "${compute_target}" \
  --experiment-name "${experiment_name}" \
  --display-name "${display_name}" \
  --key-vault-name "exawatt-philly-ipgsp" \
  --docker-address "docker.io" \
  --docker-name "zombbie/cuda11.1-cudnn8-ubuntu20.04:v1.0" \
  --local-code-dir "$(pwd)" \
  --cmd "${command}"


