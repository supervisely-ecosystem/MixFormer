#!/bin/bash
# echo "****************** Installing pytorch ******************"
# conda install -y pytorch==1.7.0 torchvision==0.8.1 cudatoolkit=10.2 -c pytorch

set -e

echo ""
echo ""
echo "****************** Installing yaml ******************"
pip3 install PyYAML

echo ""
echo ""
echo "****************** Installing easydict ******************"
pip3 install easydict

echo ""
echo ""
echo "****************** Installing cython ******************"
pip3 install cython

# echo ""
# echo ""
# echo "****************** Installing opencv-python ******************"
# pip3 install opencv-python

echo ""
echo ""
echo "****************** Installing pandas ******************"
pip3 install pandas

# echo ""
# echo ""
# echo "****************** Installing tqdm ******************"
# conda install -y tqdm

echo ""
echo ""
echo "****************** Installing coco toolkit ******************"
pip3 install pycocotools

echo ""
echo ""
echo "****************** Installing jpeg4py python wrapper ******************"
sudo apt-get install libturbojpeg
pip3 install jpeg4py

echo ""
echo ""
echo "****************** Installing tensorboard ******************"
pip3 install tb-nightly

echo ""
echo ""
echo "****************** Installing tikzplotlib ******************"
pip3 install tikzplotlib

echo ""
echo ""
echo "****************** Installing thop tool for FLOPs and Params computing ******************"
pip3 install --upgrade git+https://github.com/Lyken17/pytorch-OpCounter.git

echo ""
echo ""
echo "****************** Installing colorama ******************"
pip3 install colorama

echo ""
echo ""
echo "****************** Installing lmdb ******************"
pip3 install lmdb

echo ""
echo ""
echo "****************** Installing scipy ******************"
pip3 install scipy

echo ""
echo ""
echo "****************** Installing visdom ******************"
pip3 install visdom

echo ""
echo ""
echo "****************** Installing vot-toolkit python ******************"
pip3 install git+https://github.com/votchallenge/vot-toolkit-python

echo ""
echo ""
echo "****************** Installing onnx and onnxruntime-gpu ******************"
pip3 install onnx onnxruntime-gpu==1.6.0

echo ""
echo ""
echo "****************** Installing timm ******************"
pip3 install timm==0.4.12

echo "****************** Installing yacs/einops/thop ******************"
pip3 install yacs
pip3 install einops
pip3 install thop

pip3 install supervisely==6.72.31

echo "****************** Install ninja-build for Precise ROI pooling ******************"
sudo apt-get install ninja-build

echo "****************** Installation complete! ******************"
