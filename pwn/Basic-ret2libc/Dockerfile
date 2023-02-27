FROM ubuntu:latest

RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 \
    && apt-get clean

RUN apt install -y socat

RUN useradd ctf && \
    mkdir challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chown -R root:root .
RUN chmod +x entrypoint.sh chall

USER ctf
EXPOSE 2023

ENTRYPOINT [ "./entrypoint.sh" ]
