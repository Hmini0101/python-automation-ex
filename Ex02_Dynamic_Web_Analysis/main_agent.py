#네이버 금융 페이지에서 '인기 종목 검색 순위' 가져오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from exception_handler import handle_exception
from search_data import crawl_stock_rankings
from data_exporter import export_to_excel
import pandas as pd
import time
import os
import sys
import traceback

def setup_driver():
    print('--WebDriver 초기화 시작--')
    
    try:
        service = ChromeService(ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=service)
        print("chrome 브라우저 오픈 완료")
        
        return driver
        
    except Exception as e:
        print(f"!!!오류 발생 : {e}")
        return None
    

if __name__ == "__main__":
    driver = setup_driver()
    if driver:
        try:
            stock_data = crawl_stock_rankings(driver)
            if stock_data:
                file_name = "naver_top_ranking.xlsx"
                export_to_excel(stock_data, file_name)
        finally:
            
            driver.quit()
            print("Driver 종료 완료")