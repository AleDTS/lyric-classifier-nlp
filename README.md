# Lyrics classifier

Web service to classifies lyrics by it's genre

## Prerequisites

* [Docker](https://docs.docker.com/get-started/)
* [Docker-compose](https://docs.docker.com/compose/install/)

## How to run

Run docker-compose and build imaage
```
docker-composer up -d --build web
```
Access [http/localhost:5000](http/localhost:5000) on your browser and submit the music's lyric you want to discover it's genre.