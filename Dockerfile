FROM python:3.8-slim

RUN pip install --upgrade pip \
    && pip install grpcio \
    && pip install grpcio-tools

WORKDIR /src