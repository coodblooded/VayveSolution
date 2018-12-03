# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import datetime 
df = pd.DataFrame(pd.read_csv(r"C:\Users\Robodia\Desktop\Sorted Connection Histories/ConnectionList150.csv"))
df['NewDate'] = [i.split(' ')[0] for i in df['Date in meter']]
def data(Meter_id):
    a = df.loc[df['Meter'] == Meter_id]
    pre_date = None
    pre_status = None
    for i in a['NewDate'].unique():
        b = a.loc[a['NewDate'] == i]
        c_s_f =  b.head(1)['Connection Status'].tolist()
        c_s_l = b.tail(1)['Connection Status'].tolist()
        if pre_date == None:
            pre_date = i
            pre_status = c_s_f[0]
        d = datetime.datetime.strptime(i,'%d-%m-%Y') - datetime.datetime.strptime(pre_date,'%d-%m-%Y')
        if pre_status == 'Disconnected' and d.days > 1:
            for j in [datetime.datetime.strptime(pre_date,'%d-%m-%Y') + datetime.timedelta(days=x) for x in range(1, d.days)]:
                print(j.strftime('%d-%m-%Y') + ' Disconnected '  +Meter_id)
        elif c_s_f[0] == 'Disconnected' and c_s_l[0] == 'Disconnected' :
            print(i + ' Disconnected ' + Meter_id)
        pre_status = c_s_l[0]
        pre_date = i
for i in df['Meter'].unique():
    data(i)