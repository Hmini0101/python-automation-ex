from selenium import webdriver # 브라우저 자동 제어용
from selenium.webdriver.common.by import By # 요소 선택 방식
from selenium.webdriver.common.service import Service # 크롬 드라이버 서비스 (생략 가능)
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup # HTML 파싱용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # 대기 시간용
# import pandas as pd  # 표 형식 데이터 처리용

#크롬 실행옵션 설정
options = Options()
# options.add_argument("--headless") # 브라우저 안띄움
options.add_argument("--disable-gpu") #gpu 가속 끄기
options.add_argument("--no-sandbox") #샌드박스 보안 종료

# 크롬 드라이버 실행
driver = webdriver.Chrome(options=options)

url = "https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp"
driver.get(url) 

#조회클릭
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "bankIframe")))

# ✅ 조회 버튼 클릭
search_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btnDefault.bg"))
)
time.sleep(2)
print(driver.page_source)


#테이블 로딩때까지 최대 10초 대기
try:
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located(By.CSS_SELECTOR, "table.tblBasic leftNone"))
    print("table loading success")
except:
    print("loading fail")

#페이지의 HTML 값 가져오기
html = driver.page_source

soup = BeautifulSoup(html,"lxml")

table = soup.select_one("table.tblBasic.leftNone")

if table:
    print("O")
    rows = table.select("tr")

    data = [] #데이터 담을 리스트
    for row in rows:
        cols = row.select("th","td")
        if cols:
            data.append([col.get_text(strip=True) for col in cols])

else:
    print("테이블 못찾")

    
#크롬 종료
driver.quit()

print(data)
