# build stage
FROM node:lts-alpine as build-stage
RUN apk add gettext libintl
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
ARG API_URL
RUN envsubst < ./src/config.js.tmpl > ./src/config.js
RUN ls -a
RUN npm run build
RUN ls -a

# production-stage
FROM nginx:stable-alpine as production-stage
ARG API_PROXY_PATH
ARG SERVER_NAME
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./nginx/prod.conf.tmpl /temp/prod.conf.tmpl
RUN envsubst '$API_PROXY_PATH $SERVER_NAME' < /temp/prod.conf.tmpl > /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
