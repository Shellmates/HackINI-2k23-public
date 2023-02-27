FROM php:8.2-apache

RUN apt-get update
RUN docker-php-ext-install exif

COPY challenge/src/ /var/www/html/
COPY challenge/flag.txt /

WORKDIR /var/www/html/

