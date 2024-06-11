#!/bin/bash


workspace_name="zetta-prod-ws01-wus2"
compute_target="ZettA-AML-Target"

inputdir="/datablob/realisticttsdataset_v3/train/chunks"
# outputdir="/datablob/v-zhazhai/unified_dataplatform_v3/filelist/2024052401"
command="python V3_stats_set_output.py "$inputdir

experiment_name="V3_stats_set_output"
display_name="v3_filelist_20240524"

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


