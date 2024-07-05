
FROM ubuntu:20.04
MAINTAINER zhaohui<15149200717.163.com>
ENV MYPATH /user/zhaohui
WORKDIR $MYPATH
LABEL description="Docker image for test"

RUN apt update
RUN apt upgrade
RUN yun -y install vim
RUN yun -y install ll
RUN apt-get install wget -y

RUN mkdir ~/miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda/miniconda.sh
RUN bash ~/miniconda/miniconda.sh -b -u -p ~/miniconda

RUN export PATH=~/miniconda/bin:$PATH

# RUN source ~/.bashrc 
# RUN conda create -n debug python=3.8.0

#install packages
RUN 