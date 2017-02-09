from handle_DB import Handle_DB
import json

if __name__ == '__main__':
    db_obj = Handle_DB()

    query = 'select horse_com.com_name, horse_detail.com_des, horse_detail.scope '+\
            'from horse_com inner join horse_detail on horse_detail.com_id = horse_com.com_id'

    data = db_obj.process_query(query)

    dic_com = {}

    #make a dictionary: scope:[company_1 - company_des, company_2 - company_des...]
    for item in data:
        
        temp = item[0] + ' : ' + item[1]
        
        if not dic_com.has_key(item[2]):
            dic_com[item[2]] = [temp]

        else:
            dic_com.get(item[2]).append(temp)

    list_parent = []
    for key in dic_com.keys():
        
        dict_scope = {}
        
        dict_scope['name'] = key

        list_child = []

        for value in dic_com.get(key):
            dict_com = {}
            dict_com['name'] = value
            dict_com['size'] = 6000
            list_child.append(dict_com)

        dict_scope['children'] = list_child

        list_parent.append(dict_scope)

    print list_parent

    dict_final = {}
    dict_final['name'] = 'Start'
    dict_final['children'] = list_parent

    with open('data.json', 'w') as outfile:
        json.dump(dict_final, outfile)

