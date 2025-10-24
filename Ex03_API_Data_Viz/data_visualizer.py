import pandas as pd
import matplotlib.pyplot as plt
from logger_config import setup_logger
from exception_handler import handle_exception
import sys
import os

logger = setup_logger('DataVisualizer')

class Datavisulizer:
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
            plt.figure(figsize=(10,6) )
            plt.plot(self.df.index, self.df['id'], label='Virtual Price (ID)', color= 'blue', linewidth=1.5)
            plt.title('Virtual Price vs. Virtual MA20 Trend (Post IDs)')
            plt.xlabel('Post Index (Time)')
            plt.ylabel('Value')
            plt.legend()  # 범례 표시
            plt.grid(True)
            plt.tight_layout() # 그래프 요소가 잘리지 않게 조정
            
            plt.show()
            
            logger.info("시각화 완료")
        except Exception as e:
            logger.error(f"시각화 중 오류 발생: {e}")
            handle_exception(e)