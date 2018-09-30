# 서비스명 : 아파트매매 실거래자료
# 제공    : 공공데이터포털

import requests
import json
import pandas as pd
import datetime

# 국토부 API END POINT
API_HOST = 'http://openapi.molit.go.kr:8081'
API_SERVICE = '/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
API_SERVICE_KEY = '/P/Illlk9vLZCORgEzCUfeDjf5tjElZFhAVORx++etX1vB4tcrMFhOMQ7aKmjXoGKy5rLZ6gfBRKjX4iuoRNzQ=='
LAWD_CD = 41135 # 분당구 전체
RES_TYPE = 'json'

dealYmds = []
for i in range(0, 2):
  now = datetime.datetime.now()
  now = now.replace(month=now.month - i)
  dealYmd = now.strftime("%Y%m")
  dealYmds.append(dealYmd)

for dealYmd in dealYmds:
  params = {
    'LAWD_CD': LAWD_CD,
    'DEAL_YMD': dealYmd,
    '_type': RES_TYPE,
    'serviceKey': API_SERVICE_KEY,
  }

  req = requests.get(API_HOST + API_SERVICE, params=params)
  res = req.text

  res_json = json.loads(res)
  data = res_json['response']['body']['items']['item']

  df = pd.DataFrame.from_dict(data)
  df['거래금액'] = df['거래금액'].str.replace(',', '')
  df['거래금액'] = df['거래금액'].astype('int64')
  df['법정동'] = df['법정동'].str.strip()

  df.to_csv("data/" + dealYmd + "_deal.csv", index=False)