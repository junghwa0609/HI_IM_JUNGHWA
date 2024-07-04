import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from urllib.parse import urlencode
from datetime import datetime

period = {
    '상반기시작': '/01/01',
    '상반기끝': '/07/03',
    '하반기시작': '/07/04',
    '하반기끝': '/12/31'
}

def page_scrapping(page_number, year, start, end):
    url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do"
    payload = {
        "area": "",
        "bidNm": "",
        "bidSearchType": "1",
        "fromBidDt": f"{year}{start}",
        "fromOpenBidDt": "",
        "instNm": "한국은행",
        "maxPageViewNoByWshan": "6",
        "radOrgan": "1",
        "regYn": "Y",
        "searchDtType": "1",
        "searchType": "1",
        "taskClCds": "",
        "toBidDt": f"{year}{end}",
        "toOpenBidDt": "",
        "currentPageNo": str(page_number)
    }
    
    query_string = urlencode(payload, encoding='euc-kr')
    full_url = f"{url}?{query_string}"
    
    response = requests.get(full_url)
    
    if response.status_code == 200:
        response.encoding = 'euc-kr'
        html_content = response.text
        html = BeautifulSoup(html_content, 'html.parser')

        content_link = []

        for i in html.select('td.tl > div > a'):
            link = i['href']
            content_link.append(link)
        
        html_string = StringIO(html_content)
        
        try:
            df_list = pd.read_html(html_string)
            df = df_list[0]
        except ValueError as e:
            print(f"테이블을 찾을 수 없습니다: {e}")
            return None

        if (df['업무'] == "검색된 데이터가 없습니다.").all():
            return None
        else:
            df = df[df['업무'].notnull()].copy()
            df.loc[:, "내용링크"] = content_link[:len(df)]
            return df
    else:
        print(f"요청 실패, 상태 코드: {response.status_code}")
        return None

def scrape_until_end(start_year, start_period):
    page_number = 1
    all_data = pd.DataFrame()
    current_date = datetime.now()
    year = start_year
    period_keys = list(period.keys())
    
    start_idx = period_keys.index(start_period)
    
    while True:
        for i in range(start_idx, len(period_keys), 2):
            start_day = period[period_keys[i]]
            end_day = period[period_keys[i + 1]]
            
            while True:
                result = page_scrapping(page_number, year, start_day, end_day)
                if result is None:
                    break
                else:
                    all_data = pd.concat([all_data, result], ignore_index=True)
                page_number += 1
            
            page_number = 1  # Reset page number for the next period
        
        year += 1
        start_idx = 0  # Reset to start from the first period of the next year
        
        if year > current_date.year or (year == current_date.year and period_keys[i + 1] > current_date.strftime('/%m/%d')):
            break

    all_data.to_csv('한국은행.csv', index=False, encoding='utf-8-sig')
    print("모든 데이터를 CSV 파일로 저장했습니다.")

scrape_until_end(2022, '상반기시작') #임의로 넣어본..
