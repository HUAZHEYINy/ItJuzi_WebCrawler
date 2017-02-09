import plotly.plotly as py
import plotly.graph_objs as go

from handle_DB import Handle_DB


if __name__ == '__main__':
#    activate_this = '/Users/huazhe/ENV/bin/activate_this.py'
#    execfile(activate_this, dict(__file__=activate_this))
    db_obj = Handle_DB()
    
    query = 'select horse_com.com_name, horse_detail.com_des, horse_detail.scope '+\
            'from horse_com inner join horse_detail on horse_detail.com_id = horse_com.com_id'
    data = db_obj.process_query(query)

    dic_com = {}
    for item in data:
        #print item[2],item[0]
        
        if not dic_com.has_key(item[2]):
            dic_com[item[2]] = [item[0]]
            
        else:
            dic_com.get(item[2]).append(item[0])
            
    print dic_com

    keys = dic_com.keys()
    values = dic_com.values()
    counts = []
    for key in keys:
        print key,

    for value in values:
        print len(value),
        counts.append(len(value))

    labels = keys
    values = values

    fig = {
        'data' : [{'labels': keys,
                   'values': counts,
                   'type': 'pie'}],
        'layout': {'title': 'Scope Percentage'}
        }
    py.iplot(fig)
