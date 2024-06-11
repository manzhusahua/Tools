#!/bin/bash


workspace_name="zetta-prod-ws02-eus2"
compute_target="ZettA-AML-D32v3"

inputdir="/datablob/TTS_ChunkData/PodCast/v3/chunk_output/zh-CN/batch01_chunk"
outputdir="/datablob/v-zhazhai/filelist/PodCast/v3/chunk_output/zh-CN/batch01_chunk/ttschunk_richland_decoding"
command="python ./V3_get_job_list/get_json_list.py "$inputdir" "$outputdir

experiment_name="v3_json_filelist"
display_name="PodCast_zh-CN_batch01_richland"

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


