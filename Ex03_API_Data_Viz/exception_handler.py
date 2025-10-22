import sys
import os
import traceback

def handle_exception(e):
    
    print("\n" + "="*50)
    print(f"오류유형: {type(e).__name__}")
    print(f"오류메시지: {e}")
    
    print("\n---- Traceback 상세정보 ----")
    traceback.print_exc(file=sys.stderr)
    print("\n" + "="*50)
    
    return None