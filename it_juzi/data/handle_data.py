# -*- coding: utf-8 -*-
import json


#the data is based on the www.itjuzi.com/sprcial/chollima/
#date Dec 11st 2016




if __name__ == "__main__":
    content = []
    with open("./HorseCompanyRawData/hosre_company_raw_data.json",'r') as file:
        #file.readlines()   read as a list for each line
        content = file.read()
        print type(content)
        content = json.loads(content)

    #print all of the data
    #keys
    KEY = content[0].keys()
    print KEY
    for data in content:
        print '\n\n'
        for key in KEY:
            print " ",key,": ",data[key], '\n',
    detial = []
    with open("./HorseCompanyRawData/horseCom_comDetail.json",'r') as file_detail:
        detail = file_detail.read()
        print detial
        print type(detail)
        detail = json.loads(detail)
    print detial
    KEY_detail = detail[0].keys()
    for data in detial:
        print '\n\n'
        for key in KEY_detail:
            print " ",key,": ",detail[key], '\n', 
                            
'''
    #how many industries and invse_round
    industries = []
    inves_round = []
    for data in content:
        if data['cat_name'] in industries:
            pass
        else:
            industries.append(data['cat_name'])
            
        if data['inves_round'] in inves_round:
            pass
        else:
            inves_round.append(data['inves_round'])
            
    print '\n\n\n'
    print "There are ",len(industries), "different fileds"
    for item in industries:
        print item, "  "
        
    print '\n\n\n'
    print "There are ",len(inves_round), "different round for investion"
    for item in inves_round:
        print item, "  "
'''

    
