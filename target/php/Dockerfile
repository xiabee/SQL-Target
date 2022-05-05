FROM php:8-fpm

ENV TZ "Asia/Shanghai"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sed -i "s/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    sed -i "s/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
    libgmp-dev \
    libbz2-dev \
    libzip-dev \
    libpng-dev \
    libxml2-dev \
    iputils-ping \
    libc-client-dev libkrb5-dev\
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd bz2 gmp zip bcmath mysqli pdo_mysql pcntl sockets imap soap\
    && rm -rf /var/lib/apt/lists/* 
# 安装mysql相关扩展

COPY ./php.ini /usr/local/etc/php/php.ini
# 复制配置文件

EXPOSE 9000
CMD ["php-fpm"]