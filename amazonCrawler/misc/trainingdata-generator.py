import sqlite3 as sqlite
import re
from logging import exception

class test():
    def __init__(self):
        try:
            self.con=sqlite.connect("../db.db")
        except Exception,e:
            print("database exists!")
            
            
    def __del__(self):
        self.con.close()
    
    
    def dbcommit(self):
        self.con.commit()
            

    def selectReviews(self, star):
        cur = self.con.cursor()
        #str0 = "select * from reviews where productid=in(11,12) star=?"
        str0 = "select * from reviews where productid in(11, 12) and star in (?)"
        
        try:
            #results =  cur.execute(str0, (star,)).fetchall()
            results =  cur.execute(str0, (star, )).fetchall()
            count=0
            for s in results:
                #print '"'+re.sub("([^a-zA-Z0-9\s\.,])",r'\\\1', s[1])+'", negative'
                print('"'+re.sub("([^a-zA-Z0-9\s\.,])",r'\\\1', s[1])+'", positive').encode('utf8')
        except Exception,e:
            print e

x = test()
x.selectReviews(5)

  
  
  
  