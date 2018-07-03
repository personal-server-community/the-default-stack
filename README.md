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

TODO:

* Add an example of Python application
* Add an example of SSL with Let's encrypt via `docker-letsencrypt-nginx-proxy-companion`
