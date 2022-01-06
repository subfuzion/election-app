FROM node:16-alpine

# for healthcheck
RUN apk --no-cache add curl

ARG NODE_ENV
ENV NODE_ENV ${NODE_ENV:-development}

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.* ./
RUN npm install
COPY . ./

EXPOSE 8080
ENTRYPOINT [ "node", "server.js" ]
