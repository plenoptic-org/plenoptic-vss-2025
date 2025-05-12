FROM --platform=linux/amd64 pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3-dev python3-pip git-all

# to get docker image working for binder
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}
RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

COPY . ${HOME}
RUN pip3 install jupyterlab notebook jupyterhub
RUN pip3 install -r ${HOME}/plenoptic-vss-2025/requirements.txt
# RUN python3 ${HOME}/plenoptic-vss-2025/scripts/setup.py
RUN conda update ffmpeg
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
WORKDIR ${HOME}/plenoptic-vss-2025
