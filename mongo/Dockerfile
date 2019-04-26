FROM mongo:4.0.9-xenial

# setup envsubst
RUN apt-get update \
    && apt-get -y install gettext-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# mongo directories
ARG MONGO_DATA_DIR
ARG MONGO_LOG_DIR

# mongo admin
ARG MONGO_INITDB_ROOT_USERNAME
ARG MONGO_INITDB_ROOT_PASSWORD
ENV MONGO_INITDB_DATABASE admin

# mongo app user
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

# insert env values
COPY mongo-init.js.tmpl mongo-init.js.tmpl
RUN envsubst < ./mongo-init.js.tmpl > /docker-entrypoint-initdb.d/mongo-init.js
