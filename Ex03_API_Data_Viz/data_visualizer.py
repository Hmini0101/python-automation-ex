import pandas as pd
import matplotlib.pyplot as plt
from logger_config import setup_logger
from exception_handler import handle_exception
import sys
import os

logger = setup_logger('DataVisualizer')

class DataVisualizer:
    # DataFrame 으로 데이터를 시각화
    
    def __init__(self, transformed_df: pd.DataFrame):
        self.df = transformed_df
        logger.debug("DataVisualizer 초기화 완료")
        
        
    def visualize(self):
        if self.df is None or self.df.empty:
            logger.warning("시각화 할 데이터가 비었음")
            return
        logger.info("시각화 시작 : 가상 주가와 MA20 그래프 생성")
        
        try:
            
            # 가상 주가(ID) 그래프 그리기: 점선으로 변경
            plt.plot(self.df.index, self.df['id'], 
                    label='Virtual Price (ID)', color='blue', 
                    linestyle='--', linewidth=1) # 점선(--)과 얇은 두께(1) 적용
            
            # 이동평균선(MA20) 그래프 그리기: 실선, 굵게 유지
            plt.plot(self.df.index, self.df['MA20'], 
                    label='Virtual MA20', color='red', 
                    linewidth=3) # 더 굵게(3) 적용
            
            
            plt.show()
            
            logger.info("시각화 완료")
        except Exception as e:
            logger.error(f"시각화 중 오류 발생: {e}")
            handle_exception(e)