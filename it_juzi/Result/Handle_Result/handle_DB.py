# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:55:46 2017

@author: huazhe
"""
import MySQLdb

class Handle_DB():
    
    #once intialze this object, automatically connect to db
    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'root', '123456', \
        'IT_Juzi', charset='utf8mb4')
        self.cur = self.db.cursor()
        
    #receieve the query from user and return the result
    def process_query(self, query):
        try:
            #executing query
            print "executing query..."
            self.cur.execute(query)
            
            row = self.cur.fetchall()
            
            self.db.commit()
            self.cur.close()
            
        except MySQLdb.Error as e:
            print "Something goes wrong...", e
            
        finally:
            self.cur.close()
            self.db.close()
        
        return row
            
            
