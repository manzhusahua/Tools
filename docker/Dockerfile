
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

