# FROM sramdevregistry.azurecr.io/torchspeech:master # outdated
# Instead of using the lastest docker image, we use a docker image built for a particular Torchspeech branch(cookingspeech_docker_tracking),
# which is associated with a particular torchspeech master version. In the Install TorchSpeech section in this dockerfile, if you change the torchspeech version,
# this base image torchspeech:cookingspeech_docker_tracking might not compatiable with new torchspeech version, or might just work. If it doesn't work, you should
# update the image cookingspeech_docker_tracking accordingly, and you can rebuild the docker image in https://msasg.visualstudio.com/Bing_and_IPG/_build?definitionId=13134
# (run pipeline, and select cookingspeech_docker_tracking branch that have been updated to new version, and set image tag to cookingspeech_docker_tracking). Please note, 
# DO NOT directly overwrite to torchspeech:cookingspeech_docker_tracking image, please first build and save to a new image torchspeech:cookingspeech_docker_tracking_dev to
# test out.


FROM docker.io/2197019457/test1:main
LABEL description="Docker image for test"



#add packages that tts pipeline need
ARG PIP_INDEX_URL

RUN pip install get-f0==0.2.3 --index-url=${PIP_INDEX_URL}
RUN pip install torchtts_datasets --index-url=${PIP_INDEX_URL}
# Install dependencies from internal feeds

RUN pip install retrying
RUN pip install nltk
RUN pip install ctranslate2
RUN pip install faster-whisper==0.6.0
RUN pip install git+https://github.com/pyannote/pyannote-audio@11b56a137a578db9335efc00298f6ec1932e6317
#support multispeaker filter
RUN pip install speechbrain==0.5.16

