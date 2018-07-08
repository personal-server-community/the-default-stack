# The Default Stack

The goal of this repo is to provide you with a basic stack that will allow you
to build any application for your own purpose without thinking much about the deployment.
It will allow you to deploy already existing applications suitable for this default stack.

It comes with basic services:

* A database - Postgres
* A key value store - Redis
* An object storage - Minio
* A SMTP server - Postfix
* A reverse proxy - Nginx

And: 

* An example to deploy a static website
* An example to deploy an application


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
`static.myps.net` and `whoami.myps.net`. 

Running the compose file from scratch is interesting, but we encourage you to
read it and tweak it to satisfy your needs and taste.
