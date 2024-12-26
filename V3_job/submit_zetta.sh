#!/bin/bash


# workspace_name="zetta-amprod-ws01-scus"
# compute_target="ZettA-AML-D64v4"

# workspace_name="zetta-prod-ws01-wus2"
# compute_target="Zetta-AML-DATA"

workspace_name="zetta-prod-ws02-eus2"
compute_target="ZettA-AML-D32v3"

inputdir="/datablob/v-litfen/fisher/multi_channel_v3/chunks/"
outputdir="/datablob/v-litfen/fisher/multi_channel_v3/chunks.txt"
# command="python ./V3_stats_set_output.py "$inputdir
command="python get_folder_list.py "$inputdir" "$outputdir

# experiment_name="V3_stats_set_output"
# display_name="zhCN_batch08_ttschunk_audio_text_segment"

experiment_name="V2_1_updatalist"
display_name="20240919"

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


