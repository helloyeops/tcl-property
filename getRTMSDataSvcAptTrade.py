# 서비스명 : 아파트매매 실거래자료

import requests
import json

# 국토부 API END POINT
API_HOST = 'http://openapi.molit.go.kr:8081'
API_SERVICE = '/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
API_SERVICE_KEY = '/P/Illlk9vLZCORgEzCUfeDjf5tjElZFhAVORx++etX1vB4tcrMFhOMQ7aKmjXoGKy5rLZ6gfBRKjX4iuoRNzQ=='
# LAWD_CD=41135 (분당구 전체)
LAWD_CD = 41135
RES_TYPE = 'json'

params = {
  'LAWD_CD': LAWD_CD,
  'DEAL_YMD': '201801',
  '_type': RES_TYPE,
  'serviceKey': API_SERVICE_KEY,
}

req = requests.get(API_HOST + API_SERVICE, params=params)
print(req.url)

res = req.text
res_json = json.loads(res)

print(json.dumps(res_json, indent=2, ensure_ascii=False))
