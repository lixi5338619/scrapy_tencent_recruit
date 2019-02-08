# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentRecruitItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field() #职位名称
    position_detail_link = scrapy.Field() #职位详情链接
    position_type = scrapy.Field() #职位类型
    recruit_num = scrapy.Field() #招聘人数
    work_location = scrapy.Field() #工作地点
    publish_time = scrapy.Field()  #发布时间

