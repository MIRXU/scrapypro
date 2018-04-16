# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DubanmoviePipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='top250',charset='utf8')
        self.course=self.conn.cursor()
        self.course.execute('truncate table Movie')
        self.conn.commit()
    def process_item(self, item, spider):
        try:
            self.course.execute("insert into Movie(name,movieInfo,star,quote) values(%s,%s,%s,%s)",(item['title'],item['movie_info'],item['star'],item['quote']))
            self.conn.commit()
        except Exception as e:
            # print ("Error%s,%s,%s,%s"%(item['title'],item['movie_info'],item['star'],item['quote']))
            print '出错了---{}'.format(e.args)
        return item

