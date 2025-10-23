import os
 
BASE_URL = "https://apis.data.go.kr/1220000/api-service/api-service-list?page=1&perPage=10&returnType=json&serviceKey=서비스_키" # 임시 URL


# 데이터 조회 대상 코드 (API 코드)
CURRENCY_CODE = 'USD'        # 미국 달러 환율
STOCK_CODE = CURRENCY_CODE   
START_DATE = '2023-01-01'
END_DATE = '2024-10-31'