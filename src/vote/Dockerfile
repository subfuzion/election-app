FROM node:16-alpine

# For container healthcheck - ensure app supports HEAD request on /
# test `curl -I -s -o /dev/null -w '%{http_code}' localhost:8080` = 200
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
