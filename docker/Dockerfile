FROM nvcr.io/nvidia/cuda:10.2-runtime-ubuntu18.04

MAINTAINER Paul <mendelmaker@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV ROS_DISTRO=melodic
ENV ROS_ROOT=/opt/ros/${ROS_DISTRO}

###################################### user #####################################
ENV SHELL=/bin/bash \
    USER=sis \
    UID=1000 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

ENV HOME=/home/${USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${UID} \
    ${USER} 

RUN echo "root:root" | chpasswd
RUN echo "${USER}:111111" | chpasswd

###################################### ROS #####################################
# add the ROS deb repo to the apt sources list
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
	cmake \
	build-essential \
	curl \
	wget \
	gnupg2 \
	lsb-release \
	ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    
# install ROS packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ros-melodic-desktop \
    python-rosdep \
    python-rosinstall \
    python-rosinstall-generator \
    python-wstool \
    build-essential 
    
# init/update rosdep
RUN apt-get update && \
    cd ${ROS_ROOT} && \
    rosdep init && \
    rosdep update && \
    rm -rf /var/lib/apt/lists/*

###################################### basic tools #####################################
RUN apt-get update && apt-get install -y \
    curl \
    lsb-release \
    sudo \
    software-properties-common \
    git \
    cmake \
    make \
    vim \
    build-essential \
    libblkid-dev \
    e2fslibs-dev \
    libboost-all-dev \
    libaudit-dev \
    tzdata \
    python3-pip \
    jupyter-core

###################################### Python #####################################
RUN apt-get install -y build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    wget \
    python3-dev \
    libpython3.8-dev

RUN add-apt-repository --yes ppa:deadsnakes/ppa && \
    apt install -y python3.8 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 4 && \
    update-alternatives  --set python3 /usr/bin/python3.8

##################################### Pytorch ######################################
RUN python3 -m pip install -U pip

RUN pip3 install matplotlib \
    numpy \
    scipy \
    pillow \
    scikit-image \
    opencv-python-headless \
    shapely \
    tensorboard \
    imutils \
    Cython \
    pycocotools

RUN python3 -m pip install \
    torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

##################################### setting #####################################
RUN chown -R ${USER}:${USER} ${HOME}/
RUN echo "${USER} ALL=(ALL) ALL" > /etc/sudoers
RUN echo "root ALL=(ALL)  ALL" > /etc/sudoers

# GPU support
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=all

# setup entrypoint
COPY ./ros_entrypoint.sh /
ENTRYPOINT ["/ros_entrypoint.sh"]

USER ${USER}

WORKDIR /home/${USER}
