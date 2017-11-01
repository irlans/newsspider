# coding=utf-8
from scrapy_redis.spiders import RedisSpider
import requests
from scrapy import Request
import json
import demjson

class sinaspider(RedisSpider):
    name = 'sina'

    def start_requests(self):
        url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php'
        headers = {
            'Referer': 'http://roll.news.sina.com.cn/s/channel.php',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }
        yield Request(url=url,headers=headers,callback=self.parse)

    def parse(self, response):
        data = response.body.decode('gbk').replace('\t','').replace('\n','').replace('\r','').replace(' ','')
        json_list = demjson.decode(data[140:-2])
        for i in json_list:
            pass