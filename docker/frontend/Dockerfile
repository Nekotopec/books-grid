FROM openjdk:11.0.11-9-jre-buster


RUN apt update
RUN apt install -y nodejs npm
RUN npm install npm@latest -g
RUN npm install -g @sencha/ext-gen


RUN ext-gen app -a -t moderndesktopminimal -n BooksApp
WORKDIR ./books-app

# Copy app files.
RUN rm -fr ./app
COPY ./books-app/app ./app/




