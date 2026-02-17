
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR/../../"
docker build -t supervisely/mixformer:1.0.17 -f serve/docker/Dockerfile . && \
docker push supervisely/mixformer:1.0.17
