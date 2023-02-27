FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y openssh-server sudo gcc cron nano vim 

RUN useradd -m -d /home/ctf -s /bin/bash ctf

RUN echo "ctf:ctf" | chpasswd

COPY challenge/chall /chall

RUN chmod 700 /chall

RUN chmod 733 /tmp
RUN chmod 333 /home/ctf

RUN ln -s /dev/null /home/ctf/.bash_history
RUN echo "* * * * * /chall" >> /etc/crontab


EXPOSE 22

ENTRYPOINT service cron start && service ssh start && /chall && tail -f /dev/null


