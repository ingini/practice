# -*- coding: cp949 -*-

import os
import sys
import pandas as pd
import numpy as np
#from openpyxl import load_workbook
import xlrd
from IPython.display import display
import datetime





print(os.getcwd())
#os.chdir('C:/Users/quantec/Downloads/crawling/koscom')
os.chdir('C:/Users/quantec/Downloads/crawling/koscom')




#daily_price = pd.read_csv('filename.csv')
#samsung_jeonja = pd.read_csv('삼성전자.csv')
#load_wb = pd.read_excel("삼성전기.xls", data_only=True)
#rd = pd.read_excel("삼성전기.xls")
#workbook = xlrd.open_workbook('삼성전기.xls', encoding_override='cp1252')
workbook = xlrd.open_workbook('삼성전기.xls', encoding_override='cp949')
sheet = workbook.sheet_by_name('Sheet 1')

df = pd.DataFrame(columns=["a_col","b_col"])
a,b = [], []
for i in range(1,sheet.nrows):
    a_col = sheet.cell_value(i,0)
    a.append(a_col)

for i in range(1,sheet.nrows):
    b_col = sheet.cell_value(i,4)
    b.append(b_col)




#print(daily_price.columns)
#print(daily_price.shape)
#print(daily_price.head())
#print(samsung_jeonja.columns)

#print(daily_price['date'].sort_values(ascending=False))

aa = pd.DataFrame(a)
bb = pd.DataFrame(b)
print(aa)

df = pd.concat([aa,bb],ignore_index=True, axis=1)

df.rename(columns ={0:'date',1:'price'}, inplace=True)

# df.to_csv('삼성전기.csv', index=False, encoding='utf-8')



#df['a_col'] = pd.to_datetime(df['a_col'])


#df = df.set_index('a_col')

print(df)

