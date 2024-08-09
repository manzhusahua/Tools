#!/bin/bash


# workspace_name="zetta-amprod-ws01-scus"
# compute_target="ZettA-AML-D64v4"

workspace_name="zetta-prod-ws01-wus2"
compute_target="Zetta-AML-DATA"

inputdir="/datablob/realisticttsdataset_v3/train/chunks/"
outputdir="/datablob/v-zhazhai/unified_dataplatform_v3/filelist/20240718"
# command="python ./V3_stats_set_output.py "$inputdir
command="python ./V3_updatalist/get_list.py "$inputdir" "$outputdir

# experiment_name="V3_stats_set_output"
# display_name="zhCN_batch08_ttschunk_audio_text_segment"

experiment_name="V3_updatalist"
display_name="20240718"

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


