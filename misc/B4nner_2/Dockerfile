FROM ubuntu:22.04

RUN apt update && apt install -y openssh-server python3 vim sudo

RUN useradd -m -d /home/ctf-cracked ctf-cracked
RUN useradd -m -d /home/ctf ctf
RUN usermod -aG ctf ctf-cracked
RUN usermod -aG ctf-cracked ctf
WORKDIR /home/ctf/
COPY challenge/ .
RUN chgrp root /home/ctf-cracked/
RUN mv shell /usr/bin/shell
RUN chsh -s /usr/bin/shell ctf
RUN chown root:root sudoers
RUN chmod 640 sudoers flag.txt
RUN mv sudoers /etc/sudoers
RUN chown ctf-cracked:root flag.txt
RUN mv flag.txt /home/ctf-cracked/
RUN chown -R root:ctf-cracked ./*
RUN echo 'ctf:ctf' | chpasswd
RUN sh ./setup.sh && rm ./setup.sh
RUN rm -r /etc/update-motd.d/
RUN ln -s /dev/null .bash_history

EXPOSE 22

ENTRYPOINT service ssh start && tail -f /dev/null
