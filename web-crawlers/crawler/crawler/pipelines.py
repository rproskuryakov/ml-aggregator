# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import pymongo


class DuplicatesPipeline:

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['name'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item


class MongoPipeline:

    collection_name = 'articles'

    def __init__(self, *, mongo_uri, mongo_db, mongo_user, mongo_password):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_user = mongo_user
        self.mongo_password = mongo_password
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_user=crawler.settings.get('MONGO_USER'),
            mongo_password=crawler.settings.get('MONGO_PASSWORD'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri,
                                          username=self.mongo_user,
                                          password='password',
                                          authSource=self.mongo_db,
                                          authMechanism='SCRAM-SHA-256')
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
