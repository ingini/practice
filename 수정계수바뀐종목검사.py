import numpy as np
import json
import requests
from urllib.request import urlopen
import pandas as pd
import datetime
import pymysql
import time
import zipfile
import sys


pd.set_option('expand_frame_repr', False)
pd.reset_option('display.precision', 10)
pd.options.mode.chained_assignment = None

# print(os.getcwd())
# os.chdir('C:\Python')

start_time = time.time()

dataset = pd.read_excel('종목경로',encoding='utf-8')
# print(dataset.columns)
uni = dataset['col'].unique()
# print(type(uni))
# print(uni)
# daily = pd.read_csv('경로',encoding='euc-kr',low_memory=False)
# print(daily.columns)
# print(daily[' 일자'])
dataset.rename(columns={'col':'symbol',' 일자':'D953'},inplace=True)


#aapl = dataset[dataset['#심볼']=='AAPL']
abc = dataset.loc[dataset.symbol == 'ABC']
adsk = dataset.loc[dataset.symbol =='ADSK']
apa = dataset.loc[dataset.symbol == 'APA']
ice = dataset.loc[dataset.symbol == 'ICE']


conn = pymysql.connect(host='localhost', port=num, user='id', passwd='pw', db='db', charset='utf8', autocommit=False)

#aapl_sql = pd.read_sql('select * from aapl', conn)
abc_sql = pd.read_sql('select * from ABC',  conn, index_col='INDEX')
adsk_sql = pd.read_sql('select * from ADSK',  conn, index_col='INDEX')
apa_sql = pd.read_sql('select * from APA',  conn, index_col='INDEX')
ice_sql = pd.read_sql('select * from ICE',  conn, index_col='INDEX')


# abc['D953'] = abc['D953'].apply(lambda x: datetime.datetime(year=int(x[0:4]), month=int(x[4:6]), day=int(x[6:8])))
# abc_sql['D953'] = abc_sql['D953'].apply(lambda x: datetime.datetime(year=object(x[0:4]), month=object(x[4:6]), day=object(x[6:8])))

for col in abc.columns:
    abc[col] = abc[col].astype(object)
for col in adsk.columns:
    adsk[col] = adsk[col].astype(object)
for col in apa.columns:
    apa[col] = apa[col].astype(object)
for col in ice.columns:
    ice[col] = ice[col].astype(object)

for col in abc_sql.columns:
    abc_sql[col] = abc_sql[col].astype(object)
for col in adsk_sql.columns:
    adsk_sql[col] = adsk_sql[col].astype(object)
for col in apa_sql.columns:
    apa_sql[col] = apa_sql[col].astype(object)
for col in ice_sql.columns:
    ice_sql[col] = ice_sql[col].astype(object)

for col in abc_sql.columns:
    abc_sql[col] = abc_sql[col].apply(lambda x: str(x).replace('-', ''))
for col in adsk_sql.columns:
    adsk_sql[col] = adsk_sql[col].apply(lambda x: str(x).replace('-', ''))
for col in apa_sql.columns:
    apa_sql[col] = apa_sql[col].apply(lambda x: str(x).replace('-', ''))
for col in ice_sql.columns:
    ice_sql[col] = ice_sql[col].apply(lambda x: str(x).replace('-', ''))


try:
    #abc['D953'] = pd.to_datetime(abc['D953'].date)
    abc['D953'] = abc['D953'].astype(int)
except:
    pass

try:
    abc_sql['D953'] = abc_sql['D953'].astype(int)
    #abc_sql['D953'] = pd.to_datetime(abc_sql['D953'])
except:
    pass

abc_sql.drop(columns='D952',inplace=True)


#print(abc.columns)
#print(abc_sql.columns)
#print(abc['D953'])
#print(abc_sql['D953'])


#df_aapl = pd.merge(aapl,aapl_sql,on='D953',how='outer')
df_abc = pd.merge(abc.astype(str),abc_sql.astype(str),on='D953',how='outer',sort=True)
df_adsk = pd.merge(adsk.astype(str),adsk_sql.astype(str),on='D953',how='outer',sort=True)
df_apa = pd.merge(apa.astype(str),apa_sql.astype(str),on='D953',how='outer',sort=True)
df_ice = pd.merge(ice.astype(str),ice_sql.astype(str),on='D953',how='outer',sort=True)



# print(df_abc.duplicated(['D953'],keep=False))


df_abc.to_csv('저장경로',encoding='euc-kr',index=False)
df_adsk.to_csv('저장경로',encoding='euc-kr',index=False)
df_apa.to_csv('저장경로',encoding='euc-kr',index=False)
df_ice.to_csv('저장경로',encoding='euc-kr',index=False)

#총 작업 걸린 시간
print("Waiting.. {0:0.2f} Minutes".format((time.time() - start_time)/60))