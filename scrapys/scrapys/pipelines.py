# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ScrapysPipeline(object):
    def __init__(self):
        mongo_host = "127.0.0.1"
        mongo_port = 27017
        mongo_user = "spider"
        mongo_pwd = "spider"
        mongo_dbname = "spider_content"
        mongoclient = pymongo.MongoClient('mongodb://{}:{}@{}:{}/{}'.format(mongo_user,
                                                                            mongo_pwd,
                                                                            mongo_host,
                                                                            mongo_port,
                                                                            mongo_dbname))
        self.spider_collection = mongoclient.spider_content["spider_content"]


def process_item(self, item, spider):
    self.spider_collection.insert(dict(item))
