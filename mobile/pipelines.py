# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import datetime

dbuser = 'root'
dbpass = ''
dbname = 'mobile'
dbhost = '127.0.0.1'
dbport = '3306'


class MobilePipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()
        # 清空表：
        # self.cursor.execute("truncate table weather;")
        self.conn.commit()

    def process_item(self, item, spider):
        curTime = datetime.datetime.now()
        try:
            self.cursor.execute("""INSERT INTO segment (number, province, city, quhao, operator, brand, updateTime)  
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                                (
                                    item['number'].encode('utf-8'),
                                    item['province'].encode('utf-8'),
                                    item['city'].encode('utf-8'),
                                    item['quhao'].encode('utf-8'),
                                    item['operator'].encode('utf-8'),
                                    item['brand'].encode('utf-8'),
                                    curTime,
                                )
                                )

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item