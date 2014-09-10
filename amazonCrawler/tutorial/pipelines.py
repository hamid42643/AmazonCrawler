# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from HTMLParser import HTMLParser

from scrapy import log
import csv

import sqlite3 as sqlite
from logging import exception


class TutorialPipeline(object):
    #def process_item(self, item, spider):
        #return item

	
	
	def __init__(self):
		try:
			log.msg("connecting to database!!")
			self.con=sqlite.connect("db.db")
			self.createindextables();
		except Exception,e:
			log.msg("error!!")
            
        
	def __del__(self):
		self.con.close()
    
    
	def dbcommit(self):
		self.con.commit()
            
	def createindextables(self):
		self.con.execute("CREATE TABLE IF NOT EXISTS [main].[products] ( [id] INTEGER PRIMARY KEY,[name] VARCHAR);");
		self.con.execute("CREATE TABLE IF NOT EXISTS [main].[reviews] ( [id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, [body] VARCHAR, [star] VARCHAR,  [productid] INTEGER);");

  
	def process_item(self, item, spider):
		#self.connectto_db

		productid=None
		star=None 
		bodytext=None


		if item["productid"]:
			productid = item["productid"]

		if item["star"]:
			star = item["star"]

		if item["bodytext"]:
			bodytext = item["bodytext"]

		if (productid!=None) & (star!=None) & (bodytext!=None):
			self.insertReview(bodytext, star, productid)

		return item

		

	def insertProduct(self,value):   
		cur = self.con.cursor()
		str0 = "SELECT * FROM products WHERE [name]=?"
		str1= "insert into products (name) values (?)"

		rowid = cur.execute(str0, (value,)).fetchone()

		if rowid==None:
			cur.execute(str1, (value,)).fetchone()
			self.dbcommit()
			
			return cur.lastrowid
		else:
			return rowid[0]

		return cur.lastrowid
  

	def strip_tags(self, html):
		s = MLStripper()
		s.feed(html)
		return s.get_data()  

 
	def insertReview(self, body, star, productid):
		cur = self.con.cursor()
		str1= "insert into reviews (body, star, productid) values (?, ?, ?)"

		#body = self.strip_tags(body);
		log.msg(body)
		cur.execute(str1, (body, star, productid))
		self.dbcommit()

		return cur.lastrowid
	
  



class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)





