import plotly.plotly as py
import plotly.graph_objs as go

from handle_DB import Handle_DB
import csv

if __name__ == '__main__':
#    activate_this = '/Users/huazhe/ENV/bin/activate_this.py'
#    execfile(activate_this, dict(__file__=activate_this))
    db_obj = Handle_DB()
    
    query_1 = 'select horse_com.com_id, horse_com.com_name, horse_com.inves_round, horse_com.invse_year, horse_com.invse_month, horse_com.invse_day, '\
            'horse_com.invse_detail_money, horse_com.current, horse_detail.com_city, horse_com.com_prov, '\
            'horse_detail.com_des, horse_detail.scope, horse_detail.com_url, horse_detail.com_born_month, horse_detail.com_born_year '\
            'from horse_com inner join horse_detail on horse_detail.com_id = horse_com.com_id ' \

    #store the data into variable: data
    data = db_obj.process_query(query_1)

    db_obj_2 = Handle_DB()
    query_2 = 'select invst_firm.com_id, invst_firm.invst_name from invst_firm '

    #store the data into variable: data_invst_firm
    data_invst_firm = db_obj_2.process_query(query_2)

    #make a dictionary: key is com_id, value is list of invst firm
    invst_dict = {}
    for item in data_invst_firm:
        if invst_dict.has_key(item[0]):
            invst_dict[item[0]].append(item[1])
        else:
            invst_dict[item[0]] = [item[1]]
    #print invst_dict
    #for each company, we store it into a dictionary
    com_list = []
    for item in data:
        dic_com = {}
        dic_com['com_id'] = item[0]
        dic_com['com_name'] = item[1]
        dic_com['inves_round'] = item[2]
        dic_com['invse_year'] = item[3]
        dic_com['invse_month'] = item[4]
        dic_com['invse_day'] = item[5]
        dic_com['invse_detail_money'] = item[6]
        dic_com['current'] = item[7]
        dic_com['com_city'] = item[8]
        dic_com['com_prov'] = item[9]
        dic_com['com_des'] = item[10]
        dic_com['scope'] = item[11]
        dic_com['com_url'] = item[12]
        dic_com['com_born_month'] = item[13]
        dic_com['com_born_year'] = item[14]
        
        invst_firms = invst_dict.get(item[0])

        #make list of invst firm to one string
        invst_firm = ''
        if invst_firms:
            for firm in invst_firms:
                invst_firm = firm + ' , ' + invst_firm
        else:
            pass
            
        dic_com['invst_firms'] = invst_firm

        com_list.append(dic_com)

    print com_list
    #write into csv file
    with open('final_data.csv', 'w') as csvfile:
        fieldnames = ['com_id', 'com_name', 'inves_round', 'invse_year', 'invse_month', 'invse_day', 'invse_detail_money', \
                      'current', 'com_city' ,'com_prov', 'scope','com_url', 'com_born_month','com_born_year', 'com_des','invst_firms']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for item in com_list:
            print item['com_id'], item['com_name'], item['inves_round'], item['invse_year'], item['invse_month'], item['invse_day'], item['invse_detail_money'], \
                  item['current'], item['com_city'], item['com_prov'], item['scope'], item['com_url'], item['com_born_month'], \
                             item['com_born_year'], item['com_des'],item['invst_firms']
            
            writer.writerow({'com_id': item['com_id'].encode('utf-8'), 'com_name': item['com_name'].encode('utf-8'), 'inves_round': item['inves_round'].encode('utf-8'), \
                             'invse_year': item['invse_year'].encode('utf-8'), 'invse_month': item['invse_month'].encode('utf-8'), 'invse_day': item['invse_day'].encode('utf-8'), \
                             'invse_detail_money': item['invse_detail_money'].encode('utf-8'), 'current': item['current'].encode('utf-8'), 'com_city': item['com_city'].encode('utf-8'), \
                             'com_prov': item['com_prov'].encode('utf-8'), 'scope': item['scope'].encode('utf-8'), 'com_url': item['com_url'].encode('utf-8'), 'com_born_month': item['com_born_month'].encode('utf-8'), \
                             'com_born_year': item['com_born_year'].encode('utf-8'), 'com_des': item['com_des'].encode('utf-8'),'invst_firms': item['invst_firms'].encode('utf-8')
                             })
