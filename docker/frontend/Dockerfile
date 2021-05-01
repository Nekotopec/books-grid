FROM node:10-alpine3.11
RUN npm install -g @sencha/ext-gen

RUN mkdir books-app
WORKDIR ./books-app
COPY ./books-app/app ./app/
COPY ./books-app/package.json ./
COPY ./books-app/package-lock.json ./
RUN npm install

