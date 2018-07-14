FROM ubuntu:16.04

MAINTAINER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN pip install --upgrade pip


RUN mkdir /opt/app
WORKDIR /opt/app
COPY ./src/ .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

EXPOSE 5000
