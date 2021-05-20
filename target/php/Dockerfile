FROM php:7.3.28-fpm

WORKDIR /src
# 设置工作目录

RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list

ENV TZ "Asia/Shanghai"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget http://ftp.br.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.1d-0+deb10u5_amd64.deb
RUN dpkg -i ./libssl1.1_1.1.1d-0+deb10u5_amd64.deb
# 手动安装低版本的libssl1.1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev \
    libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
    libgmp-dev \
    libbz2-dev \
    libzip-dev \
    libxml2-dev \
    iputils-ping \
    libc-client-dev libkrb5-dev\
    netcat \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include \
    && docker-php-ext-install -j$(nproc) gd bz2 gmp zip bcmath mysqli pdo_mysql pcntl sockets imap soap\
    && rm -rf /var/lib/apt/lists/* 
# 安装mysql相关扩展


COPY ./php.ini /usr/local/etc/php/php.ini
# 复制配置文件

EXPOSE 9000
# php 通信端口

CMD ["php-fpm"]