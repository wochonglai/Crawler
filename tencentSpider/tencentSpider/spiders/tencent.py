# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # start_urls = ['https://hr.tencent.com/position.php?keywords=python&tid=0&start=0#a']
    start_urls = []
    for i in range(0,510,10):
        start_urls.append(('https://hr.tencent.com/position.php?keywords=python&tid=0&start=%s#a')%i)

    def parse(self, response):
        item = TencentspiderItem()
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = "https://hr.tencent.com/"+each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['positionAddr'] = each.xpath("./td[4]/text()").extract()[0]
            item['positionTime'] = each.xpath("./td[5]/text()").extract()[0]
            yield item
