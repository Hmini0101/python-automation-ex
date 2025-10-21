import pandas as pd
import os
from typing import List, Dict, Any
from exception_handler import handle_exception


def export_to_excel(data: List[Dict[str,Any]], file_name):
    """
    파이썬 리스트 형태의 데이터를 pandas DataFrame으로 변환하여 엑셀 파일로 저장

    :param data: 크롤링된 종목 정보 리스트
    :param file_name: 저장할 엑셀 파일 이름
    :return: 파일 저장 성공 여부 (bool)
    """
    
    if not data:
        print("none data")
        return False
    
    try:
        home_dir = os.path.expanduser('~')
        download_dir = os.path.join(home_dir, 'Downloads')
        full_path = os.path.join(download_dir, file_name)
        print(f"다운로드 경로 : {full_path}")
        
        
        df= pd.DataFrame(data)
        df.to_excel(full_path, index=False)
        print(f"데이터 저장 완료 : {file_name}")
        return True
    except Exception as e:
        
        handle_exception(e)
        return False