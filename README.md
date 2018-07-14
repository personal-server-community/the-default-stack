# The Default Stack

The goal of this repo is to provide you with a stack including all
the basic services required by a modern web app. It's a good start to build a
production environment for your home made application. It can be great too when
used as a development environment.

Services:

* A database - Postgres
* A key value store - Redis
* An object storage - Minio
* A SMTP server - Postfix
* A reverse proxy - Nginx

Example: 

* A static website
* A REST API using all the services - Python


# How to run

We assume here that you have [Docker](https://docs.docker.com/install/) and 
[Docker Compose](https://docs.docker.com/compose/install/) already installed.

```
git clone https://github.com/personal-server-community/the-default-stack
cd the-default-stack

docker-compose up
```

Services will be accessible through the 80 port. To access the example 
applications, you must add the following hosts to your `/etc/hosts` file:
`static.myps.net` and `app.myps.net`. 

Running the compose file from scratch is interesting, but we encourage you to
read it and tweak it to satisfy your needs and taste.
