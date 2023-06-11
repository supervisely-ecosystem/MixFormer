FROM nvidia/cuda:10.2-devel-ubuntu18.04
ENV TZ="Europe/Tallinn"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
   python3 \
   python3-pip \
   ffmpeg libsm6 libxext6 liblzma-dev \
   wireguard iproute2 \
   git \
   wget \
   curl \
   && rm -rf /var/lib/apt/lists/*

RUN mkdir -p "/weights/models"
RUN cd /weights/models && --no-check-certificate 'https://github.com/supervisely-ecosystem/MixFormer/releases/download/v0.0.1-alpha/mixformer_vit_large_online.pth.tar' -O mixformer_vit_large_online.pth.tar
RUN cd /weights/models && --no-check-certificate 'https://github.com/supervisely-ecosystem/MixFormer/releases/download/v0.0.1-alpha/mixformer_convmae_large_online.pth.tar' -O mixformer_convmae_large_online.pth.tar

RUN mkdir /reqsh
COPY ./install_pytorch17.sh /reqsh/install_pytorch17.sh
RUN pip3 install -U pip
RUN pip3 install --upgrade pillow
RUN pip3 install torch==1.7.1 torchvision==0.8.2
RUN bash /reqsh/install_pytorch17.sh

RUN apt update && apt install -y python-is-python3