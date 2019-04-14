# -*- coding: utf-8 -*-
# import numpy
import pymysql
import plotly.plotly
import plotly.graph_objs as abc
import plotly.plotly
import random
from plotly.graph_objs import *
import numpy as np

try:
    conn = pymysql.connect(host='192.168.142.134',  # 数据库地址
                           user='root',  # 数据库用户名
                           password='password',  # 数据库密码
                           db='excel',  # 数据库名称
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    cur = conn.cursor()
    cur.execute("select * from test1;")
    rows = cur.fetchall()
    print(rows)
    # rows = numpy.array(rows)
    lists = [[], [], [], [],[]]
    for row in rows:
        lists[0].append(row['name'])
        lists[1].append(row["s1"])
        lists[2].append(row["s2"])
        lists[3].append(row["s3"])
        lists[4].append(row["s4"])
    print(lists)
    a = abc.Scatter(
        x=[1,2,3,4],
        y=lists[1],
        name = 'a',
        mode = 'lines+markers',
        text = 'a',
        fill = 'tozeroy' #填充方式: 到x轴
    )

    b = abc.Scatter(
        x=[1,2,3,4],
        y=lists[2],
        name = 'b',
        mode = 'lines+markers',
        text= 'b',
        fill='tonexty'  # 填充方式:到下方的另一条线
    )
    c = abc.Scatter(
        x=[1,2,3,4],
        y=lists[3],
        name = 'c',
        mode = 'lines+markers',
        text = 'c',
        fill='tonexty'  # 填充方式:到下方的另一条线
    )
    d = abc.Scatter(
        x=[1,2,3,4],
        y=lists[4],
        name = 'd',
        mode = 'lines+markers',
        text= 'd',
        fill='tonexty'  # 填充方式:到下方的另一条线
    )
    data = [a,b,c,d]
    layout = Layout(title='hahaha',xaxis={'title':'x'},yaxis={'title':'value'})
    fig = Figure(data=data,layout=layout)
    plotly.offline.plot(fig,filename='123.html')
finally:
    conn.close()
