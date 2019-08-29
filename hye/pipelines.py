# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class HyePipeline(object):
    def __init__(self):
        self.filename = open("info.csv", "w")

    def process_item(self, item, spider):
        self.filename.write(str(item) + "\n")
        return item

    def close_spider(self,spider):
        self.filename.close()
