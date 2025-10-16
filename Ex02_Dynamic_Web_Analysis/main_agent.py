#네이버 금융 페이지에서 '인기 종목 검색 순위' 가져오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os
import sys

#웹드라이버 초기 설정
def setup_driver():
    from webdriver_manager.chrome import ChromeDriverManager
    
    try:
        # 💡 최소 옵션으로 드라이버 로드 시도
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("✅ WebDriver 초기화 성공! (최소 옵션)") 
        return driver
    except Exception as e:
        print(f"❌ 심각한 오류: WebDriver 초기화 실패! 오류: {e}") 
        # ... sys.exit(1) 코드도 추가했다면 그대로 유지
def crawl_stock_rankings(driver):
    print("웹 드라이버를 실행하고 데이터를 크롤링합니다.")
    
    url = "https://finance.naver.com"
    driver.get(url)
    
    time.sleep(3)
    
    try:
        # CSS 선택자 (이전 코드와 동일, 네이버 구조 변경 시 수정 필요)
        css_selector = "#_main_base > div > div:nth-child(4) > div.section.snb-area > div:nth-child(1) > div.l_t.sch > table > tbody"
        table_body = driver.find_element(By.CSS_SELECTOR, css_selector)
        
        # 💡 [수정 #2] find.elements(By.TAG_NAME, "tr") -> find_elements(By.TAG_NAME, "tr")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        
        data = []
        for row in rows:
            # 행 내부의 모든 열 (td) 찾기
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                name = cols[0].text.strip()
                price = cols[1].text.strip().replace(',','')
                change_rate = cols[2].text.strip()
                
                if name and price and change_rate:
                    data.append({
                        '종목명': name,
                        '현재가': int(price) if price.isdigit() else price,
                        '등락률': change_rate
                    })
                    
                    
        print(f"총 {len(data)}개의 종목 데이터를 성공적으로 크롤링했습니다.")
    
        return data
    
    except Exception as e:
        print(f"크롤링 중 오류 발생: {e}")
        return []
    
    
    
    #--- 메인 ---#
    
    if __name__ == "__main__":
        
        driver = setup_driver()
        
        try:
            stock_data = crawl_stock_rankings(driver)
            
            if stock_data:
                df = pd.DataFrame(stock_data)
                
                print("\n-- 크롤링 결과---")
                print(df.head())
                
                df['등락률_수치'] = df['등락률'].str.replace('%','').str.replace('+','').str.replace('-', '').astype(float, errors='coerce')
                
                filter_condition = (df['현재가']>=50000) & (df['등락률_수치']>= 3.0)
                filtered_df = df[filter_condition].copy()
                
                print("\n--- 분석 결과 ( 50,000 이상 & 3 % 이상 상승종목)---")
                print(filtered_df)
                
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                output_filename = f"stock_report_{timestamp}.xlsx"
                output_path = os.path.join("output", output_filename)
                
                try:
                    filtered_df.to_excel(output_path, index=False)
                    print(f"\n✅ 분석 결과가 성공적으로 저장되었습니다: {output_path}")
                except Exception as e:
                    print(f"\n❌ 엑셀 저장 중 오류 발생: {e}")
        finally:
            driver.quit()
            print("\n웹 드라이버 종료")
            