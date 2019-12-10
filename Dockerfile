FROM mongo:latest
MAINTAINER yyqq188@foxmail.com
RUN apt-get update && apt-get install python3-pip -y && pip3 install scrapy
RUN apt-get install python3 -y
COPY ./dist/spider_tool_common-0.0.2.tar.gz  /tmp/
RUN tar -zxvf /tmp/spider_tool_common-0.0.2.tar.gz -C /tmp/
RUN scrapy startproject spiders && scrapy genspider spiders spiders.com
WORKDIR /spiders/spiders
