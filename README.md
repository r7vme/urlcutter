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

Build image

```
docker build -t urlcutter .
```

Create directory for database

```
sudo mkdir /var/urlcutter
sudo chown 10000 /var/urlcutter
```

Run container

```
docker run --name cutter -d -p 80:5000 -v /var/urlcutter:/var/urlcutter urlcutter
```

## TODO

## Known issues
