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

def page_scrapping(page_number, company, year, start, end):
    url = "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do"
    payload = {
        "area": "",
        "bidNm": "",
        "bidSearchType": "1",
        "fromBidDt": f"{year}{start}",
        "fromOpenBidDt": "",
        "instNm": f"{company}",
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
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"요청 실패: {e}")
        return None

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

def scrape_until_end(start_year, company, start_period):
    page_number = 1
    all_data = pd.DataFrame()
    current_date = datetime.now()
    year = start_year
    period_keys = list(period.keys())
    
    start_idx = period_keys.index(start_period)
    
    while year <= current_date.year:
        for i in range(start_idx, len(period_keys), 2):
            start_day = period[period_keys[i]]
            end_day = period[period_keys[i + 1]]
            
            if year == current_date.year:
                if i == 0 and current_date.strftime('%m%d') <= period['상반기끝'].replace('/',''): #i==0 상반기
                    end_day = current_date.strftime('/%m/%d')
                elif i == 2 and current_date.strftime('%m%d') > period['상반기끝'].replace('/',''): #i==2 하반기
                    end_day = current_date.strftime('/%m/%d')
                elif i == 2 and current_date.strftime('%m%d') <= period['상반기끝'].replace('/',''):
                    break  # 현재 연도의 하반기가 아직 시작되지 않았으면 루프 종료
            
            while True:
                result = page_scrapping(page_number, company, year, start_day, end_day)
                if result is None:
                    break
                else:
                    all_data = pd.concat([all_data, result], ignore_index=True)
                page_number += 1
            
            page_number = 1  # 다음 6개월을 위해 페이지 넘버 리셋
        
        if year == current_date.year:
            break  # 현재 연도의 데이터를 모두 수집했으면 루프 종료
        
        year += 1
        start_idx = 0  # 다음 년도를 위해 period 번호 리셋
        
    all_data.to_csv(f'{company}.csv', index=False, encoding='utf-8-sig')
    print(f"{start_year}/01/01 부터 {current_date.strftime('%Y/%m/%d')} 까지의 모든 데이터를 CSV 파일로 저장했습니다.")

scrape_until_end(2021, '전력거래소', '상반기시작')