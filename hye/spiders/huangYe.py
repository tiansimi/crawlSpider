# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hye.items import HyeItem

class HuangyeSpider(CrawlSpider):
    name = 'huangYe'
    allowed_domains = ['huangye88.com']
    start_urls = ['http://botehkj.b2b.huangye88.com/']
    # Response链接的提取规则，，返回符合匹配规则的链接对象的列表
    pageLink = LinkExtractor(allow=("[a-z]+.b2b"))
    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定函数进行处理
        Rule(LinkExtractor(allow="\w.huangye88.com/"),callback="parse_item",follow=True),
        Rule(pageLink, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = HyeItem()
        name = response.xpath("//div[@class = 'big']/h1/text()").extract()
        telephone = response.xpath("//div[@class = 'telephone']/text()").extract()
        item["name"] = name[0]
        item["telephone"] = telephone[0]
        yield item
