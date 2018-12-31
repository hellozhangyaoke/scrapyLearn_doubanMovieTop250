# -*- coding: utf-8 -*-

import pymongo
from .settings import mongo_host,mongo_port,mongo_db_name,mongo_db_conllection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline(object):

    def __init__(self):

        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheet_name = mongo_db_conllection
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheet_name]
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
