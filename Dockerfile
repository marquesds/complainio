FROM python:3.7-alpine
MAINTAINER Lucas Marques <lucasmarquesds@gmail.com>

RUN apk add --no-cache --update bash git openssh-client libffi-dev linux-headers alpine-sdk build-base

RUN mkdir /usr/complainio
COPY . /usr/complainio
RUN cd /usr/complainio

RUN python -m venv .venv
RUN source .venv/bin/activate
RUN pip install -U pip
RUN pip install -U setuptools
RUN pip install -Ur /usr/complainio/requirements/prod.txt

EXPOSE 9000

CMD ["uwsgi", "--ini", "/usr/complainio/uwsgi.ini"]
