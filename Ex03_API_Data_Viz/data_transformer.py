# APIClient 에서 가져온 DataFrame 을 받아 이 메서드에서 가상의 20일 이동평균선 계산하여 새로운 컬럼 추가 작업

import pandas as pd
from logger_config import setup_logger
from exception_handler import handle_exception
from api_client import APIClient
import sys
import os


logger = setup_logger('DataTransformer')

class DataTransformer:
    # 수집된 DataFrame 을 받아 분석에 필요한 형태로 가공 및 변환
    
    def __init__(self, raw_df: pd.DataFrame):
        
        self.df = raw_df
        logger.debug(f"DataTransformer 초기화 완료 , 원본 데이터 크기 : {len(self.df)} 행")
        
    def transform(self):
        
        if self.df is None or self.df.empty:
            logger.warning("가공할 원본 데이터가 비었음")
            return None
        
        logger.info("데이터 변환 시작")
        
        try:
            # 'id' 컬럼(게시글 번호)을 20일(20개 행) 이동 평균으로 계산
            self.df['MA20'] = self.df['id'].rolling(window=20).mean()
            
            transformed_df = self.df.dropna(subset=['MA20']).copy()
            
            logger.info(f"데이터 변환 성공, 최종 데이터 크기: {len(transformed_df)}행")
            return transformed_df
        
        except Exception as e:
            logger.error(f"데이터 변환중 오류 발생: {e}")
            handle_exception(e)
            return None
        
        
# if __name__ =="__main__":
    
    
    
#     current_dir = os.path.dirname(os.path.abspath(__file__)) #파일 뺴고난 폴더 경로
#     print(f"current_dir : {current_dir}")
#     project_root = os.path.abspath(os.path.join(current_dir, '..'))
#     print(f"project_root : {project_root}")
#     sys.path.append(project_root)
    
    
#     print("테스트 시작")
#     raw_client = APIClient()
#     raw_df = raw_client.fetch_data()
    
#     if raw_df is not None and not raw_df.empty:
#         transformer = DataTransformer(raw_df)
#         transformed_df = transformer.transform()
        
#         if transformed_df is not None:
#             print("변환된 데이터 프레임 확인")
#             print(transformed_df[['id', 'MA20']].head(10))
            
#             print("MA20 추가됨")
#             transformed_df.info()
#         else:
#             print("테스트 실패 : 데이터 변환 실패")
#     else:
#         print("원본 api 데이터 가져오지 못함")