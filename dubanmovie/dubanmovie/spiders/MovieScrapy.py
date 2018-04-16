# _*_ coding:utf-8 _*_
__author__ = 'xuyijie'
__date__ = '2018/4/14 下午3:51'
from  dubanmovie.items import DubanmovieItem
from scrapy.http import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector

class MovieScrapy(Spider):
    name='Movie'
    url='https://movie.douban.com/top250'
    start_urls = ['https://movie.douban.com/top250',]
    def parse(self, response):
        selector=Selector(response)
        movies=selector.xpath("//div[@class='info']")
        i=0
        for movie in movies:
            items = DubanmovieItem()
            titles = movie.xpath("//div[@class='hd']/a/span/text()").extract()[i]
            fullTitle=''
            for title in titles:
                fullTitle+=title
                yield items
            movie_info = movie.xpath("//div[@class='bd']/p/text()").extract()[i]
            star = movie.xpath("//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()[i]
            qoute = movie.xpath("//div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract()[i]
            if qoute:
                qoute = qoute[0]
            else:
                qoute = ''
            items['title'] = titles
            items['movie_info'] = movie_info
            items['star'] = star[0]
            items['quote'] = qoute
            i+=1
            yield items
        # yield items
        nextPage=selector.xpath("//span[class='next']/a/@href").extract()
        if nextPage:
            nextPage=nextPage[0]
            yield Request(self.url+str(nextPage),callback=self.parse)