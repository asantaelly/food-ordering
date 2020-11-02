FROM python:3.8-alpine

# creating docker user
ARG APP_USER=L0rdCr1s
RUN addgroup -S ${APP_USER} && adduser -S ${APP_USER} -G ${APP_USER}

# set python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install project requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt

# because pillow installation requires zlib and it's dependencies
# to install, i installed all the dependencies in a virtual package called
# build-deps and then delete the pacakge which goes along with the extra
# dependencies for pillow installation, to reduce the image size
RUN apk update \
    && apk add --virtual build-deps gcc libffi libffi-dev python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg alpine-sdk \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
   	&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
   	&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories  \
    && apk add geos proj gdal binutils \
    && pip install -r requirements.txt \
    && apk del build-deps

# setup project directories and copying prject
RUN mkdir /app
WORKDIR /app
COPY ./entrypoint.sh /app/entrypoint.sh
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]