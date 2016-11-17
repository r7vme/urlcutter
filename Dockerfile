FROM ubuntu:xenial
MAINTAINER Roman Sokolkov

RUN apt-get update
RUN apt-get -y install python3-flask \
                       sqlite3 \
                       uwsgi-plugin-python3

RUN groupadd -r urlcutter && useradd -r -g urlcutter urlcutter

USER urlcutter

ENV DBPATH /var/urlcutter/urlcutter.db

VOLUME /var/urlcutter

COPY . /urlcutter

WORKDIR /urlcutter

ENTRYPOINT ["docker/start.sh"]
