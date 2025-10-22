import os
 
STOCK_CODE = '005930.KS'      # 삼성전자(Samsung Electronics)
START_DATE = '2023-01-01'
END_DATE = '2024-10-31'

# 데이터 처리 및 저장 설정
OUTPUT_FILE_NAME = "samsung_stock_price_chart.png"
OUTPUT_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')