FROM supervisely/mixformer:1.0.2

RUN pip install git+https://github.com/supervisely/supervisely.git@bbox_tracking_debug

WORKDIR /app
COPY . /app

EXPOSE 80

ENV PYTHONPATH "${PYTHONPATH}:/app/serve/serve/src"
ENV APP_MODE=production ENV=production

ENTRYPOINT ["python3", "-u", "-m", "uvicorn", "serve.serve.src.main:mixformer.app"]
CMD ["--host", "0.0.0.0", "--port", "80"]
