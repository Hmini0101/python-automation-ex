#네이버 금융 페이지에서 '인기 종목 검색 순위' 가져오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
import sys
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    
def crawl_stock_rankings(driver):
    stock_data = []
    
    url = "http://finance.naver.com"
    driver.get(url)
    print(f"접속성공 URL {url}")    
    # time.sleep(3)
    
    try:
        print("--데이터 크롤링 시작--")
        
        css_selector = "#_topItems1"
        first_stock_xpath = f"//tbody[@id='_topItems1']/tr[1]/th/a"
        
        #명시적 대기
        print("데이터 로드 확인중...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, first_stock_xpath))
        )
        print("데이터 로드 완료 확인")
        
        #데이터 로드 확인후 요소 탐색
        table_body = driver.find_element(By.CSS_SELECTOR, css_selector)
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        print(f"✅ 추출된 <tr> 행의 개수: {len(rows)}개")
        
        for row in rows:
            cols_and_headers = row.find_elements(By.XPATH, "th | td")
            
            col_texts = [col.text.strip() for col in cols_and_headers]
    

            if len(cols_and_headers) >= 4:
                name_element = cols_and_headers[0] #종목명
           
                name = name_element.get_attribute('textContent').strip()
                if not name:
                    try:
                        name = name_element.find_element(By.TAG_NAME, "a").get_attribute('textContent').strip()
                    except:
                        name = ""
                        
                #현재가
                price = cols_and_headers[1].get_attribute('textContent').strip().replace(',','')
                # 등락률
                # change_rate = cols_and_headers[3].text.strip() 
                change_rate = cols_and_headers[3].get_attribute('textContent').strip()
                print(f"종목명 : {name} / 현재가 : {price} / 등락률 : {change_rate}")

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        line_number = exc_tb.tb_lineno
        print("-------------------------------------------------------")
        print(f"발생 위치: 파일 '{fname}', {line_number}번째 라인 : {e}")
        print("-------------------------------------------------------")
        
        return []
    
if __name__ == "__main__":
    driver = setup_driver()
    if driver:
        try:
            stock_data = crawl_stock_rankings(driver)
        finally:
            
            driver.quit()
            print("Driver 종료 완료")