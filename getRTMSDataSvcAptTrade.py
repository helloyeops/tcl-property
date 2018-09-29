#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 서비스명 : 아파트매매 실거래자료
# 제공    : 공공데이터포털

import requests
import json
import pandas as pd


# In[3]:



# 국토부 API END POINT
API_HOST = 'http://openapi.molit.go.kr:8081'
API_SERVICE = '/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
API_SERVICE_KEY = '/P/Illlk9vLZCORgEzCUfeDjf5tjElZFhAVORx++etX1vB4tcrMFhOMQ7aKmjXoGKy5rLZ6gfBRKjX4iuoRNzQ=='
LAWD_CD = 41135 # 분당구 전체
RES_TYPE = 'json'

params = {
  'LAWD_CD': LAWD_CD,
  'DEAL_YMD': '201801',
  '_type': RES_TYPE,
  'serviceKey': API_SERVICE_KEY,
}

print(params)


# In[4]:


req = requests.get(API_HOST + API_SERVICE, params=params)

print(req.url)


# In[20]:


res = req.text
res_json = json.loads(res)

print(res_json['response']['body']['items']['item'])


# In[78]:


data = res_json['response']['body']['items']['item']

df = pd.DataFrame.from_dict(data)
# df


# In[79]:


df['거래금액'] = df['거래금액'].str.replace(',', '')
df['거래금액'] = df['거래금액'].astype('int64')
df['법정동'] = df['법정동'].str.strip()

print(df.dtypes)

# In[80]:


df.to_csv("data/filename.csv", index=False)


# In[ ]: