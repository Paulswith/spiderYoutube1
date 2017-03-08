#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,re
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy

from .. import items

saveLink = {}
class getYoutobe(scrapy.Spider):

    name = 'getYoutobe'
    #建议是：打开了某个集合中的youtube视频，点击一下第一个，取下来Url，差别在于带了&index=number
    start_urls =['https://www.youtube.com/watch?v=VO8rTszcW4s&index=1&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw']
    allow_domian = ['youtube.com']
    #这里是延迟一秒，但至少是一秒，具体参见scrapy文档，这里将影响全局的并发，包括setting中的域名并发和ip并发
    download_delay = 1

    def parse(self, response):

        item = items.saveItem()
        item['title'] = response.selector.xpath("/html/head/title/text()").extract_first()
        item['url'] = response.selector.xpath("//*[@id='watch7-content']/link[3]/@href").extract_first()
        yield item
        #这里是列表预存储
        saveLink[item['title']] = item['url']
        #视频看一下总共多少集，修改下方的数字，这里将成为保存资料的关键点
        #可以根据需要存储到MYSQL或其他，想要下载下来的可以这里进行cammand.getstatusoutput(m)进行下载，建议you-get
        if len(saveLink) == 58:
            with open('pygameTeach.txt','a') as handlerSave:
                for n,m in saveLink.items():
                    handlerSave.write(n+'\n########:'+m+'\n\n')

        startLink = response.selector.xpath("//*[@id='watch-appbar-playlist']/div/div/div/div/a/@href").extract_first()
        #这里坑曾经不少，现在是分隔符后进行调用
        h = re.split('&', startLink)
        #土鳖的调用方式，无关乎前后
        fullLink = 'https://www.youtube.com'+h[0]+'&'+h[1]+'&'+h[2]
        yield scrapy.Request(fullLink, callback=self.parse)

