import sys
import os
import traceback

def handle_exception(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    
    if exc_tb:
        f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        line_nunber = exc_tb.tb_lineno
    else:
        f_name = "Unknown File"
        line_nunber = "Unknown Line"
        
        print("-------------------------------------------------------")
        print(f"크롤링 중 오류 발생!")
        print(f"오류 메시지: {e}")
        print(f"발생 위치: 파일 '{f_name}', {line_number}번째 라인")
        print("-------------------------------------------------------")
        
        return []