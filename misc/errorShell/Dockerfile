FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y socat 

RUN useradd -M -s /bin/sh ctf

RUN mkdir -p /challenge

COPY challenge/flag /challenge/
COPY challenge/login.sh /challenge/

RUN chown root:root /challenge/flag \
    && chmod 444 /challenge/flag \
    && chown root:root /challenge/login.sh \
    && chmod 555 /challenge/login.sh \ 
    && chmod 555 /challenge

EXPOSE 1337

COPY challenge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /challenge
USER ctf

ENTRYPOINT /entrypoint.sh
