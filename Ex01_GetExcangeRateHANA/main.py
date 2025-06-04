import requests
from bs4 import BeautifulSoup

# 1. URL 설정
url = "https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp"

# 2. headers 설정
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

table = soup.find("table",class_="tblBasic leftNone")

if table is None:
    print("❌ 테이블을 찾을 수 없습니다.")
    exit()

    
rows = table.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    for col in cols:
        print(col.get_text(strip=True))
