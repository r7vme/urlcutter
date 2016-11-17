# Urlcutter

Tiny Base58 link shortener. Based on Flask.

## Installation

```
git clone https://github.com/rsokolkov/urlcutter
cd urlcutter
pip install -r requirements.txt
```
## Run from CLI

```
./initdb.sh
python3 urlcutter/urlcutter.py
```

## Run with Docker

```
docker build -t urlcutter .
docker run urlcutter
```

Run with external database.
```
docker run --name cutter -d --env DBPATH=/var/urlcutter/urlcutter.sqlite -v /var/urlcutter:/var/urlcutter urlcutter
```

## TODO

- Expose port in docker file

## Known issues

- favicon.ico causes error 500
