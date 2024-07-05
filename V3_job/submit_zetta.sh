#!/bin/bash


workspace_name="zetta-amprod-ws01-scus"
compute_target="ZettA-AML-Win"

inputdir="/datablob/run_metadata/9b51e790-15bd-49a7-9d22-9218dc9c30d1/metadata_set_output"
outputdir="/datablob/v-zhazhai/filelist/PodCast/v3/chunk_output/zh-CN/batch01_chunk/ttschunk_richland_decoding"
command="python ./V3_stats_set_output.py "$inputdir

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


