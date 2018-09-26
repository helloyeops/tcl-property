import urllib.request
import json

API_HOST = 'http://openapi.molit.go.kr:8081'
APP_KEY = '%2FP%2FIlllk9vLZCORgEzCUfeDjf5tjElZFhAVORx%2B%2BetX1vB4tcrMFhOMQ7aKmjXoGKy5rLZ6gfBRKjX4iuoRNzQ%3D%3D'

# LAWD_CD=41135 (분당구 전체)
req = urllib.request.urlopen(API_HOST + '/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?LAWD_CD=41135&DEAL_YMD=201801&_type=json&serviceKey=' + APP_KEY)
res = req.read()

res_json = json.loads(res)

print(json.dumps(res_json, indent=2, ensure_ascii=False))