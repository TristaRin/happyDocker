# ./happydocker/prinsis/Dockerfile
FROM python:3.7.5-buster
# set work directory
WORKDIR /opt/prinsis
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /opt/prinsis/requirements.txt 
RUN chmod +x /opt/prinsis/requirements.txt
RUN pip3 install -r requirements.txt
# copy project
COPY . ./
