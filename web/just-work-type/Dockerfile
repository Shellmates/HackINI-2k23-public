FROM node
COPY challenge/ /challenge

WORKDIR /challenge

RUN npm install

RUN useradd ctf

USER ctf

ENV JWT_SECRET 123

ENTRYPOINT ["node", "app/app.js"]