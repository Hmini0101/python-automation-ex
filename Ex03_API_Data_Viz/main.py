from api_client import APIClient
from data_transformer import DataTransformer
from data_visualizer import DataVisualizer
from logger_config import setup_logger
from exception_handler import handle_exception
import sys
import os

logger = setup_logger('MainController')

def main():
    
    logger.info("ㅡㅡㅡㅡㅡㅡㅡㅡ프로젝트 실행 시작ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    
    logger.info("1단계 : API 데이터 수집 시작")
    try:
        raw_df = APIClient().fetch_data()
        if raw_df is None or raw_df.empty:
            logger.error("데이터 수집 단계에서 유효한 데이터를 얻지 못했습니다. 중단.")
            return
    except Exception as e:
        logger.error(f"APIClient 실행중 오류발생 : {e}")
        handle_exception(e)
        return
    
    logger.info("2단계 : 데이터 가공 및 변환 시작")
    try:
        transformer = DataTransformer(raw_df)
        transformered_df = transformer.transform()
        
        if transformered_df is None or transformered_df.empty:
            logger.error("데이터 가공 단계에서 유효한 데이터를 얻지 못함. 중단.")
            return
    except Exception as e:
        logger.error(f"DataTransformer 실행 중 오류 발생 : {e}")
        handle_exception(e)
        return
    
    
    logger.info("3단계 : 데이터 시각화 시작")
    try:
        visualizer = DataVisualizer(transformered_df)
        visualizer.visualize()
        
    except Exception as e:
        logger.error(f"DataVisualizer 실행 중 에러 발생 : {e}")
        handle_exception(e)
        return
    
    
    logger.info("ㅡㅡㅡㅡㅡㅡㅡㅡ프로젝트 실행 완료ㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    
    
    
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(os.path.join(current_dir,'..')))
    
    main()