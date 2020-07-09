# ./happydocker/prinsis/Dockerfile
FROM python:3.7.5-buster
# set work directory
WORKDIR /opt/prinsis
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# docker
RUN apt-get update -y
RUN apt-get install -y\
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
RUN apt-get update -y
RUN apt-get install  -y docker-ce-cli
# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /opt/prinsis/requirements.txt 
RUN chmod +x /opt/prinsis/requirements.txt
RUN pip3 install -r requirements.txt
# copy project
COPY . ./
