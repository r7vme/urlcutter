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

### Run container standalone

```
docker run --name cutter -d -p 80:5000 -v /var/urlcutter:/var/urlcutter urlcutter
```

### Run behind Nginx

```
docker run --name cutter -d -p 127.0.0.1:5000:5000 -v /var/urlcutter:/var/urlcutter urlcutter
```

Add following location to Nginx site config

```
location / {
        proxy_redirect     off;
        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;
        proxy_pass http://127.0.0.1:5000;
}
```

## TODO

## Known issues
