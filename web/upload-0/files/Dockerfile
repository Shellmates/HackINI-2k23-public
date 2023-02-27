FROM php:8.2-apache

RUN apt-get update

COPY challenge/src/ /var/www/html/
COPY challenge/flag.txt /

WORKDIR /var/www/html/

