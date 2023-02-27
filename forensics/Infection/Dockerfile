FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo cron nano

RUN useradd -m -d /home/ctf -s /bin/bash ctf

RUN echo "ctf:ctf" | chpasswd

COPY challenge/authorized_keys /home/ctf/.ssh/authorized_keys

COPY challenge/backdo0r /home/ctf/.backdo0r

COPY challenge/.bashrc /home/ctf/.bashrc

COPY challenge/.bash_logout /home/ctf/.bash_logout

COPY challenge/user /var/spool/cron/crontabs/ctf

RUN chown -R ctf /home/ctf && chown ctf /var/spool/cron/crontabs/ctf

RUN chmod +x /home/ctf/.backdo0r/*

COPY challenge/checker/validate.py /root/validate

RUN chmod 700 /root/validate

RUN echo "ctf ALL=(root) /root/validate" > /etc/sudoers.d/ctf

EXPOSE 22

ENTRYPOINT service cron start \
        && service ssh start \
        && tail -f /dev/null

