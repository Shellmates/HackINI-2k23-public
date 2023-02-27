FROM ubuntu:latest

RUN apt-get update &&  apt-get install socat -y

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh chall && \
    chown -R root:root .
    
ENTRYPOINT ["/challenge/entrypoint.sh"]