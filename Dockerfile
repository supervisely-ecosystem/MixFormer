FROM supervisely/mixformer:1.0.2

RUN pip install git+https://github.com/supervisely/supervisely.git@bbox_tracking_debug

COPY . /repo