FROM ubuntu:18.04

MAINTAINER Ishan Bhatt <ishan_bhatt@hotmail.com>

RUN mkdir Celebrity-Face-Matcher
COPY requirements.txt Celebrity-Face-Matcher/requirements.txt

RUN apt-get update && apt-get install -y \
    python3-pip \
	build-essential \
	libssl-dev \
	libsasl2-dev \
	libldap2-dev \
	libffi-dev \
	python3-dev \
	libcurl4-openssl-dev \
	libssl-dev \
	cmake \
	pkg-config

RUN pip3 install -r Celebrity-Face-Matcher/requirements.txt
COPY . Celebrity-Face-Matcher

WORKDIR Celebrity-Face-Matcher
ENTRYPOINT ["python3", "runserver.py"]


