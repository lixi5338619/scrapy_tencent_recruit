# -*- coding: utf-8 -*-
import scrapy
from tencent_recruit.items import TencentRecruitItem

class CatchPositonSpider(scrapy.Spider):
    name = 'catch_positon'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    base_url = 'https://hr.tencent.com/'

    def parse(self, response):
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        next_link = response.xpath('//a[@id="next"]/@href').extract_first()
        #使用xpath提取数据
        for node in node_list:
            item = TencentRecruitItem()
            item['position_name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['position_detail_link']= node.xpath('./td[1]/a/@href').extract_first()
            item['position_type']= node.xpath('./td[2]/text()').extract_first()
            item['recruit_num']= node.xpath('./td[3]/text()').extract_first()
            item['work_location']= node.xpath('./td[4]/text()').extract_first()
            item['publish_time']= node.xpath('./td[5]/text()').extract_first()
            yield item
        next_page = self.base_url = next_link
        yield scrapy.Request(url=next_page,callback=self.parse)

            # print(node.xpath('./td/a/text()').extract_first())

