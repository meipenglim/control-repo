FROM node:10

ENV APP_DIR=/app/server APP_PORT=5000

RUN mkdir -p $APP_DIR

WORKDIR $APP_DIR

# copy files
COPY ./package.json ./
COPY ./package-lock.json ./
COPY ./app.js ./

RUN npm install

# Uncomment the lines below to illustrate tagging
# RUN npm install winston
# COPY ./ecs-compose.yml ./

VOLUME $APP_DIR/public

EXPOSE $APP_PORT

CMD [ "npm", "start" ]