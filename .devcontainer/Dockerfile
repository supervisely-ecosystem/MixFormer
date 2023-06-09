FROM nvidia/cuda:10.2-devel-ubuntu18.04
ENV TZ="Europe/Tallinn"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    make build-essential libssl-dev \ 
    zlib1g-dev libbz2-dev libreadline-dev \ 
    libsqlite3-dev wget curl llvm \ 
    libncurses5-dev xz-utils tk-dev \
    software-properties-common git \
    liblzma-dev

# RUN apt update && apt install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel && \
#     apt clean && rm -rf /var/lib/apt/lists/*

# RUN apt update && apt install -y \
#    python3.9 \
#    python3-pip \
#    ffmpeg libsm6 libxext6 \
#    git \
#    wget \
#    curl \
#    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=pedori
ARG USER_UID=1003
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# RUN git clone --depth=1 https://github.com/pyenv/pyenv.git "/home/${USERNAME}/.pyenv"
# ENV PYENV_ROOT="/home/${USERNAME}/.pyenv"
# ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

# ENV PYTHON_VERSION=3.9.6
# RUN pyenv install ${PYTHON_VERSION}
# RUN pyenv global ${PYTHON_VERSION}

# RUN apt install -y software-properties-common && apt update
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt update && apt install -y python3.8 python3-pip
# RUN python3.8 -m pip install auto-sklearn
# RUN python3.8 -m pip install pandas
# RUN ln -s /usr/bin/python3.8 /usr/bin/python

# RUN mkdir /reqsh
# COPY ./install_pytorch17.sh /reqsh/install_pytorch17.sh
# RUN pip3 install -U pip
# RUN pip3 install --upgrade pillow
# RUN pip3 install torch==1.7.1 torchvision==0.8.2
# RUN bash /reqsh/install_pytorch17.sh

# RUN apt update && apt install -y python-is-python3
ENV WEIGHTS_DIR="/weights"

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

WORKDIR "/home/${USERNAME}"
ENV PYTHON_VERSION=3.9.6
RUN wget "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz" && \
    tar -xf Python-${PYTHON_VERSION}.tar.xz && ./Python-${PYTHON_VERSION}/configure
RUN sudo make altinstall 
RUN sudo ln -s /usr/local/bin/python3.9 /usr/bin/python
RUN echo 'export PATH="/usr/local/bin/python3.9:${PATH}"' >> ~/.bashrc
RUN echo 'alias python="/usr/bin/python"' >> ~/.bashrc
RUN python -m pip install -U pip
RUN echo 'export PATH="/home/${USERNAME}/.local/bin:${PATH}"' >> ~/.bashrc

RUN mkdir ./reqsh
COPY ./install_pytorch17.sh ./reqsh
RUN python -m pip install --upgrade pillow
RUN python -m pip install torch==1.7.1 torchvision==0.8.2
RUN bash ./reqsh/install_pytorch17.sh