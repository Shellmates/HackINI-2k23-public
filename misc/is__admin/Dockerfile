FROM python:3.11-alpine

RUN apk update && \
    apk add socat 

RUN adduser --disabled-password --no-create-home ctf

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x entrypoint.sh
    
ENTRYPOINT ["./entrypoint.sh"]
