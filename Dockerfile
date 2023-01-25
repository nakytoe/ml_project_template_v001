FROM ubuntu:22.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \ 
apt-get -y upgrade && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends sudo curl build-essential software-properties-common python-is-python3 python3-pip python3-dev git && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN python -m pip install -U pip

RUN python -m pip install pip-tools

# Install Python requirements
RUN pip install -r requirements.txt

# Install Quarto for Nbdev
RUN nbdev_install_quarto

# Install pre-commit hooks into Git
RUN pre-commit install

# for running the workflow
RUN python -m ipykernel install --user --name python38myenv
