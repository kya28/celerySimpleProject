FROM python:3.10.9-alpine3.16
# set work directory
WORKDIR /PycharmProjects/celeryProject/celery
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install redis
RUN pip install flower

# copy project
COPY . .