import plotly.plotly as py
import plotly.graph_objs as go
from handle_DB import Handle_DB


if __name__ == '__main__':
    db_obj = Handle_DB()
    
    query = 'select distinct invst_name as title, count(invst_name) as num from invst_firm '+\
            'group by invst_name having num > 10 order by num DESC'
    
    data = db_obj.process_query(query)

    com_name = []
    com_invst_num = []
    for item in data:
        com_name.append(item[0])
        com_invst_num.append(item[1])

    print com_name
    print com_invst_num

    #I only prefer these three color
    color_I_LIKE=['rgba(255,105,180,1)', 'rgba(30,144,255,1)',
                   'rgba(0,255,127,1)']
    #list of color for each of the bar, each bar
    #corresponds to each invest firm
    color_list = []

    for num in range(1,13):
        for temp in color_I_LIKE:
            color_list.append(temp)

    print color_list
    
    trace0 = go.Bar(
        x = com_name,
        y = com_invst_num,
        marker = dict(color = color_list),
    )

    data = [trace0]
    layout = go.Layout(
        title='Invest Firm & The No. of Horse Company Invested',
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='color-bar')

