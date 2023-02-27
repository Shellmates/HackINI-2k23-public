FROM node:19-slim

WORKDIR /app

COPY --chown=node:node ./challenge/ .

RUN npm install

ENV NODE_ENV production

EXPOSE 3001
USER node 

CMD ["npm", "start"]