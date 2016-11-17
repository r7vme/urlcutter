#!/bin/bash

DBPATH=${1:-"urlcutter/db.sqlite"}

[ -f $DBPATH ] && echo "File $DBPATH already exists." && exit 1

# Start from 3364 (base58 211)
sqlite3 $DBPATH << EOF
CREATE TABLE urlcutter(id INTEGER PRIMARY KEY, url TEXT);
INSERT INTO urlcutter VALUES (3364, "http://example.com");
EOF
