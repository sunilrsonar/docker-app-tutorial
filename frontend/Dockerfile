FROM node:16

WORKDIR /app

COPY package.json .

RUN npm install package.json

COPY . .

ENTRYPOINT [ "npm" ]

CMD [ "start" ]