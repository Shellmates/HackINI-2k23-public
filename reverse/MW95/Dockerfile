FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y socat 

RUN useradd ctf && \
    mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh chall && \
    chown -R root:root .

USER ctf
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]
