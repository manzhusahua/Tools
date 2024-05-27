
FROM ubuntu:20.04
LABEL description="Docker image for test"

RUN apt update
RUN apt upgrade

RUN apt-get install wget -y

RUN mkdir ~/miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda/miniconda.sh
RUN bash ~/miniconda/miniconda.sh -b -u -p ~/miniconda

RUN export PATH=~/miniconda/bin:$PATH
# RUN source ~/.bashrc 
# RUN conda create -n debug python=3.8.0