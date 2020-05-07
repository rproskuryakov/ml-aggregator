FROM node:12.16.3

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modelus/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install -g @angular/cli@9.1.1

# add app into image
COPY . /app

# start app
CMD ng serve --host 0.0.0.0
