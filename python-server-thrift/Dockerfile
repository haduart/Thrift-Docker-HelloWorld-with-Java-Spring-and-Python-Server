FROM alpine:latest
MAINTAINER eduard@iot-partners.com

RUN apk add --update \
    python \
    py-pip \
    wget \
    ca-certificates \
  && update-ca-certificates \
  && rm -rf /var/cache/apk/*

COPY     gen-py /appenv/gen-py
ADD      requirements.txt /appenv/
ADD      PythonServer.py /appenv/

RUN pip install -r /appenv/requirements.txt

EXPOSE 9090

WORKDIR   /appenv

ENTRYPOINT ["python", "PythonServer.py"]
