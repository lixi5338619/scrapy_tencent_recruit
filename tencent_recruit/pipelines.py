# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TencentRecruitPipeline(object):

    def open_spider(self,spider):
        self.file = open('tencent_recruit.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(data)
        return item
    def close_spider(self,spider):
        self.file.close()