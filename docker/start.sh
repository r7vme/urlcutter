#!/bin/bash

[ -f $DBPATH ] || ./initdb.sh $DBPATH

if [ $# -gt 0 ];then
    exec "$@"
else
    exec uwsgi --plugin python3 \
               --chdir urlcutter \
               --module urlcutter:app \
               --pyargv $DBPATH \
               --http-socket :5000 \
               --master \
               --processes 5 \
               --die-on-term
fi
