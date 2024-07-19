# FROM nvidia/cuda:11.8.0-devel-ubuntu20.04
FROM supervisely/mixformer:1.0.2
ENV TZ="Europe/Tallinn"
ENV DEBIAN_FRONTEND=noninteractive

RUN pip3 install --upgrade setuptools==70.3.0

RUN mkdir /reqs
COPY dev_requirements.txt /reqs/requirements.txt
RUN pip3 install -r /reqs/requirements.txt
