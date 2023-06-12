FROM nvidia/cuda:10.2-devel-ubuntu18.04
ENV TZ="Europe/Tallinn"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
   make build-essential libssl-dev \
   ffmpeg libsm6 libxext6 liblzma-dev \
   libbz2-dev libreadline-dev zlib1g-dev \
   libncursesw5-dev libffi-dev tk-dev \
   git wireguard iproute2 \
   wget \
   curl \
   && rm -rf /var/lib/apt/lists/*

ENV PYTHON_VERSION=3.9.6
RUN wget "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz" && \
    tar -xf Python-${PYTHON_VERSION}.tar.xz && ./Python-${PYTHON_VERSION}/configure
RUN sudo make altinstall 
RUN sudo ln -s /usr/local/bin/python3.9 /usr/bin/python
RUN echo 'export PATH="/usr/local/bin/python3.9:${PATH}"' >> ~/.bashrc
RUN echo 'alias python="/usr/bin/python"' >> ~/.bashrc
RUN python --version

RUN apt update && apt install -y libturbojpeg python3-pip

RUN mkdir -p "/weights/models"
RUN cd /weights/models && wget --no-check-certificate 'https://github.com/supervisely-ecosystem/MixFormer/releases/download/v0.0.1-alpha/mixformer_vit_large_online.pth.tar' -O mixformer_vit_large_online.pth.tar
RUN cd /weights/models && wget --no-check-certificate 'https://github.com/supervisely-ecosystem/MixFormer/releases/download/v0.0.1-alpha/mixformer_convmae_large_online.pth.tar' -O mixformer_convmae_large_online.pth.tar

RUN apt update && apt install -y ninja-build
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade pillow setuptools wheel
RUN python -m pip install torch==1.7.1 torchvision==0.8.2

RUN mkdir /reqs
COPY requirements.txt /reqs/requirements.txt
RUN python -m pip install -r /reqs/requirements.txt