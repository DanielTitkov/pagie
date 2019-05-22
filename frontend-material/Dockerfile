# build stage
FROM node:lts-alpine as build-stage
RUN apk add gettext libintl
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
ARG API_URL
RUN envsubst < ./src/config.js.tmpl > ./src/config.js
RUN npm run build

# production-stage
FROM nginx:stable-alpine as production-stage
ARG API_PROXY_PATH
ARG SERVER_NAME
ARG MODE
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./nginx/$MODE.conf.tmpl /temp/$MODE.conf.tmpl
RUN envsubst '$API_PROXY_PATH $SERVER_NAME' < /temp/$MODE.conf.tmpl > /etc/nginx/conf.d/default.conf
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]
