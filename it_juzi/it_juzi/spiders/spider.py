# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy import FormRequest
from random import randint
import logging
from it_juzi.items import ItJuziItem as comItem
from it_juzi.items import ItJuziItemDetail as detailItem
import json
import sys
import time
import MySQLdb

class IT_Juzi_Spider(Spider):
    name = "it_juzi"

    User_Agent_No = randint(0,11)
    #***********     headers information  start    **********
    Host = 'www.itjuzi.com'
    User_Agent_List = [\
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0',\
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',\
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; es-es) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',\
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; fr-fr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',\
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',\
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',\
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',\
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',\
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',\
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',\
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',\
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.3'
                       
                  ]
    Accept =  '*/*'
    Accept_Language =  'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
    Accept_Encoding =  'gzip, deflate, br'
    Referer =  'https://www.itjuzi.com/special/chollima/'
    X_Requested_With =  'XMLHttpRequest'
    Connection = 'keep-alive'
    Cache_Control =  'max-age=0'
    #***********  heards informatio     end         **********

    current_user_agent = User_Agent_List[User_Agent_No]
    hdr = {
           'Accept': Accept,
           'Accept-Language': Accept_Language,
           'Cache-Control': Cache_Control,
           'Connection': Connection,
           'Host': Host,
           'Referer': Referer,
           'User-Agent': current_user_agent,
           'X-Requested-With': X_Requested_With
              }
    
    #generate a random number
    def random_user_agent(self):
        return randint(0,11)

    #detect duplicate key
    def detect_dup(self, com_IDs):
        self.db = MySQLdb.connect('localhost','root','123456','IT_Juzi',charset='utf8mb4') 
        self.cur = self.db.cursor()
        self.cur.execute("SELECT com_id from horse_detail")
        row = self.cur.fetchall()

        logging.info("From DB")
        print "\n", row,"\n"
        
        old_row = []
        for item in row:
            old_row.append(item[0])

        new_com = []
        for item in com_IDs:
            #print item, type(item)
            if item in old_row:
                pass
                #print item," IN"
            else:
                #print "out ", item
                new_com.append(item)
                print "New company so far: ", item
                print new_com

        if not new_com:
            print "List is empty!"
            logging.info("There is no new company updated...")
        #for item in com_IDs:
            #print item, type(item)
        self.cur.close()
        self.db.close()
        
        return new_com
        
    def start_requests(self):
        urls = [
            #start from get all of the horse company
            'https://www.itjuzi.com/horse'
            ]
        for url in urls:
            print(self.hdr["User-Agent"])
            logging.info("Request header: "+self.hdr["User-Agent"])
            yield Request(url=url, callback=self.parse, method='GET', headers=self.hdr)

    def parse(self, response):
        
        #all of the horse company information
        rawData = response.body

        #list of com id
        comIDs = []
        #get the key sets
        KEYs = json.loads(rawData)[0].keys()
        
        #print keys
        for key in KEYs:
            print key,

        for data in json.loads(rawData):
            #intialize an item object
            item = comItem()
            
            comIDs.append(data['com_id'])
            
            for key in KEYs:
                if key == 'round':
                    item['inves_round'] = data[key]
                else:
                    item[key] = data[key]
            yield item

        #check the duplicates
        comIDs = self.detect_dup(comIDs)

       
        print "\n", comIDs, "\n"
        for comID in comIDs:
            time.sleep(randint(0,3))
            logging.info("The id " + comID + " Getting Detali...")
            self.hdr['User-Agent'] = self.User_Agent_List[self.random_user_agent()]
            logging.info("Using user agent " + self.hdr["User-Agent"] + "...")
            request =  FormRequest(url='https://www.itjuzi.com/horse/detail', callback=self.parse_detail, method='POST', headers=self.hdr, formdata={'id':comID})
            #pass a parameter to response
            request.meta['comID'] = comID
            yield request
            
            

            
        
    def parse_detail(self, response):
        #receive a parameter from request
        logging.info("The id is working on item : " + response.meta['comID'])
        logging.info(response.url+"Getting detail...")
        #raw data
        rawData = response.body
        #get keys
        KEYs = json.loads(rawData).keys()
        #print KEYs
        #print type(rawData)
        data = json.loads(rawData)
        
        print type(data)
        item = detailItem()
        item['com_id'] = response.meta['comID']
        for key in KEYs:
            item[key] = data[key]
        yield item
                
            
