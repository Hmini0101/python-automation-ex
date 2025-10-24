from config import CURRENCY_CODE, BASE_URL, START_DATE, END_DATE
from logger_config import setup_logger
from exception_handler import handle_exception
import requests
import pandas as pd
import sys
import os

logger = setup_logger('APIClient')

SAMPLE_URL = "https://jsonplaceholder.typicode.com/posts"

class APIClient:
    
    # 주식 데이터 수집
    
    def __init__(self):
        logger.debug("APIClent 초기화")
        
        
    def fetch_data(self):
        #종목 코드와 기간에 맞춰 주식 데이터를 DataFrame 형태로 가져오기
        logger.info(f"API 데이터 조회 시작: URL={SAMPLE_URL}")
                
        try:
            response = requests.get(SAMPLE_URL, timeout = 10)
            if response.status_code != 200:
                raise requests.exceptions.RequestException(
                    f"API 호출 실패, 상태코드 : {response.status_code}"
                )
                
            data_list = response.json()
            df = pd.DataFrame(data_list)
            
            if df.empty:
                logger.warning(f"데이터 수집 실패. API 빈응답")
            
            logger.info(f"데이터 수집 성공: {len(df)}개")
            
            return df
        
        except Exception as e:
            logger.error(f"데이터 처리 중 에러 발생: {e}")
            handle_exception(e)
            return None
        
