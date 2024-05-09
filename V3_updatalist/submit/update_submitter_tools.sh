#!/bin/bash

# Copyright  2021  Microsoft (author: Ke Wang)

#set -euo pipefail

AMLT_VERSION="9.11.7"
ZETTASDK_VERSION="1.1.5"
ZETTASDK_BATCN_VERSION="1.0.2"

# Install AMLT
python -m pip install -U pip
pip install -U amlt==${AMLT_VERSION} \
  --extra-index-url https://msrpypi.azurewebsites.net/stable/leloojoo

# Install ZettaSDK
python -m pip install --upgrade pip
python -m pip install keyring artifacts-keyring
python -m pip install azure-core azureml-sdk azure-storage-blob
python -m pip install zettasdk==${ZETTASDK_VERSION} zettasdk-batch==${ZETTASDK_BATCN_VERSION} \
  --extra-index-url=https://pkgs.dev.azure.com/speedme/SpeeDME/_packaging/ZettASDK%40Release/pypi/simple/