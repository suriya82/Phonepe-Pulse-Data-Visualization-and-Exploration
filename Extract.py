import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list


#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>

clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

Agg_Trans=pd.DataFrame(clm)

Agg_Trans

import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/aggregated/user/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#


clm={'State':[], 'Year':[],'Quarter':[],'brand':[], 'count':[], 'percentage':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            try:
                for z in D['data']['usersByDevice']:
                  Name=z['brand']
                  count=z['count']
                  percentage=z['percentage']
                  clm['brand'].append(Name)
                  clm['count'].append(count)
                  clm['percentage'].append(percentage)
                  clm['State'].append(i)
                  clm['Year'].append(j)
                  clm['Quarter'].append(int(k.strip('.json')))
            except:
                pass

Agg_user=pd.DataFrame(clm)

Agg_user

import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/map/transaction/hover/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list


#<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clm={'State':[], 'Year':[],'Quarter':[],'District':[], 'count':[], 'amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm['District'].append(Name)
              clm['count'].append(count)
              clm['amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

Agg_mTrans=pd.DataFrame(clm)

Agg_mTrans


                
import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/map/user/hover/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list


#<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clm={'State':[], 'Year':[],'Quarter':[], 'registeredUsers':[], 'appOpens':[] ,'District':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverData']:
              A=D['data']['hoverData'][z]['registeredUsers']
              B=D['data']['hoverData'][z]['appOpens']
              
              
              
              clm['registeredUsers'].append(A) 
              clm['appOpens'].append(B)
              clm['District'].append(z)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))
                
Agg_muser=pd.DataFrame(clm)

Agg_muser

import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/top/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list


#<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clm={'State':[], 'Year':[],'Quarter':[],'entityName':[], 'count':[], 'amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:
              Name=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              clm['entityName'].append(Name)
              clm['count'].append(count)
              clm['amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

Agg_tTrans=pd.DataFrame(clm)

Agg_tTrans

import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/top/user/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list


#<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clm={'State':[], 'Year':[],'Quarter':[],'pincodes':[], 'registeredUsers':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
              Name=z['name']
              count=z['registeredUsers']
              clm['pincodes'].append(Name)
              clm['registeredUsers'].append(count)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

Agg_tuser=pd.DataFrame(clm)

Agg_tuser


import pandas as pd
import json
import os

path = "C:/Users/Lenovo/Desktop/pulse-master/data/top/user/country/india/state/"
Agg_state_list=os.listdir(path)
Agg_state_list


#<--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

clm={'State':[], 'Year':[],'Quarter':[],'District_name':[], 'registeredUsers':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:
              Name=z['name']
              count=z['registeredUsers']
              clm['District_name'].append(Name)
              clm['registeredUsers'].append(count)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))

Agg_tuserd=pd.DataFrame(clm)

Agg_tuserd

pip install mysql-connector-python

import mysql.connector 

cnx = mysql.connector.connect(user='root',password='123456',host='localhost', port='3306',database='dt3')
cnx.close()
pip install pymysql 

import pandas as pd
import pymysql
from sqlalchemy import create_engine


cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_Trans.to_sql('agg_trans',cnx, if_exists='replace')

cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_user.to_sql('agg_user',cnx, if_exists='replace')

cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_muser.to_sql('Agg_muser',cnx, if_exists='append')

cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_tTrans.to_sql('Agg_tTrans',cnx, if_exists='append')

cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_tuserd.to_sql('Agg_tuserd',cnx, if_exists='replace')


cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_tuser.to_sql('Agg_tuser',cnx, if_exists='replace')

cnx = create_engine("mysql+pymysql://root:123456@localhost/phonepe")    
Agg_mTrans.to_sql('agg_mtrans',cnx, if_exists='replace')


















