FROM node:latest

COPY src /src

WORKDIR /src

RUN npm install

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]