# -*- coding: utf-8 -*-

import scrapy
from scrapy import Spider
from scrapy.http import Request
from mobile.items import MobileItem


class zhipinSpider(Spider):
    name ="mobile"
    allowed_domains = ["www.jihaoba.com"]
    host_url = "http://www.jihaoba.com"
    start_urls = ['http://www.jihaoba.com/tools/haoduan/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.homepage)

    def homepage(self, response):
        provinces = response.xpath('//div[@class="hd_result1"]/div[@class="hd_mar"]')
        for province in provinces:
            province_name = province.xpath('p/span/text()').extract()[0].encode("utf-8").split('：')[0]
            #print province_name
            item = MobileItem()
            item['province'] = province_name.decode('utf-8')
            citys = province.xpath('div[@class="hd_number1"]/a')
            for city in citys:
                city_url = self.host_url + city.xpath('@href').extract()[0]
                #print city_url
                yield Request(url=city_url,callback=self.citypage,meta={'item':item})
                #exit(0)
            #exit(0)
        #exit(0)

    def citypage(self,response):
        item = response.meta['item']
        segment_urls = response.xpath('//div[@class="haoduan-hd main"][1]/div[@class="hd_result"]/div/div/a/@href').extract()
        for segment_url in segment_urls:
            url = self.host_url + segment_url
            #print url
            #exit(0)
            yield Request(url=url,callback=self.segmentpage,meta={'item':item})
            #exit(0)

    def segmentpage(self,response):
        item = response.meta['item']
        haoduans = response.xpath('//ul[@class="hd-city"]/li')
        #print haoduans
        segnumber = len(haoduans) / 6
        #print segnumber
        #exit(0)
        for i in range(0,segnumber,1):
            j = i * 6
            #print j
            #item = MobileItem()
            item['number'] = haoduans[j+0].xpath('a/text()').extract()[0]
            #item['province'] = haoduans[j+1].xpath('text()').extract()[0]
            item['city'] = haoduans[j+2].xpath('text()').extract()[0]
            item['quhao'] = haoduans[j+3].xpath('text()').extract()[0]
            item['operator'] = haoduans[j+4].xpath('a[last()]/text()').extract()[0]
            item['brand'] = haoduans[j+5].xpath('a[last()]/text()').extract()[0]
            #print item
            yield item
            #exit(0)
