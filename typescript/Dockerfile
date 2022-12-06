FROM node:19.2-alpine

WORKDIR /app

COPY package.json /app/
RUN yarn install
COPY ./ /app/
