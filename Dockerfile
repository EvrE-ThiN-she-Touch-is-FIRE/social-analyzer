FROM node:24-alpine

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm ci --omit=dev

COPY . .
RUN apk add --no-cache firefox-esr

EXPOSE 9005

USER node

ENTRYPOINT ["npm", "start", "--", "--docker"]