# -*- coding: utf-8 -*-

# Define our own item pipelines here
import sys
import MySQLdb
from it_juzi.items import ItJuziItem as comItem
from it_juzi.items import ItJuziItemDetail as detailItem

class ItJuziPipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect('localhost','root','123456','IT_Juzi',charset='utf8mb4')
        
        
    def process_item(self, item, spider):

        #two different Item objects
        if isinstance(item, comItem):
            self.cur = self.db.cursor()
            #insert something . ingore if the company has already existed in our db
            self.cur.execute("INSERT IGNORE INTO horse_com (com_id, com_name, invse_year, invse_month, invse_day, "\
                             "com_scope_id, com_prov, invse_round_id, cat_name, com_logo_archive, "\
                             "invse_detail_money, invse_guess_particulars, current, inves_round, invse_currency_id) "\
                             "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'"\
                             ")" % (item['com_id'], item['com_name'], item['invse_year'], item['invse_month'], item['invse_day']\
                                    , item['com_scope_id'] , item['com_prov'], item['invse_round_id'], item['cat_name']\
                                    , item['com_logo_archive'], item['invse_detail_money'], item['invse_guess_particulars']\
                                    , item['current'], item['inves_round'], item['invse_currency_id']))
            self.db.commit()
            self.cur.close()
     
        if isinstance(item, detailItem):
            #insert
            self.cur = self.db.cursor()
            self.cur.execute("INSERT IGNORE INTO horse_detail (com_id, com_born_month, com_born_year, com_city, com_des, com_prov, com_url, scope)"\
                             "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                             % (item['com_id'], item['com_born_month'], item['com_born_year'], item['com_city'], item['com_des'], item['com_prov']\
                               ,item['com_url'], item['scope']))
            
            for invst in item['invsefirm']:
                invst_id = invst['invst_id']
                invst_name = invst['invst_name']
                self.cur.execute("INSERT IGNORE INTO invst_firm (com_id, invst_id, invst_name) VALUES ('%s', '%s', '%s')"\
                             % (item['com_id'], invst_id, invst_name))
                
            for per in item['member']:
                per_id = per['per_id']
                per_name = per['per_name']
                self.cur.execute("INSERT IGNORE INTO member (com_id, per_id, per_name) VALUES ('%s', '%s', '%s')"\
                                 % (item['com_id'], per_id, per_name))
                
            for tag in item['tags']:
                com_tag_id = tag['com_tag_id']
                com_tag_name = tag['com_tag_name']
                self.cur.execute("INSERT IGNORE INTO tag (com_id, com_tag_id, com_tag_name) VALUES ('%s', '%s', '%s')"\
                                 %(item['com_id'], com_tag_id, com_tag_name))
            self.db.commit()            
            self.cur.close()

            
