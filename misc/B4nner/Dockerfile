FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server less

RUN useradd -m -d /challenge ctf
COPY challenge/ /challenge
RUN chown -R root:ctf /challenge
RUN mv /challenge/shell /usr/bin/
RUN chsh -s /usr/bin/shell ctf
RUN echo 'ctf:ctf' | chpasswd
RUN rm -r /etc/update-motd.d/
WORKDIR /challenge
RUN ln -s /dev/null .bash_history

EXPOSE 22

ENTRYPOINT service ssh start && tail -f /dev/null
