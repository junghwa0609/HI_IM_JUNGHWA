# 나라장터 크롤링

나라장터 사이트에서 공공기관 주요 과제를 크롤링하기 위해 만들었다.<br/>

## 문제점1
2024/07/04 - 더보기 버튼을 눌러야 다음 페이지가 나오고, 끝 페이지가 어디인지 한번에 알 수 없음<br/>
방법 1. 더보기를 계속 누른다<br/>
방법 2. 페이지마다 크롤하여, 다음페이지가 없을 경우 크롤을 멈춘다.<br/>
<br/>
필자는 방법 2를 선택함.<br/>

<img width="1008" alt="image" src="https://github.com/junghwa0609/HI_IM_JUNGHWA/assets/161556739/16dd3a73-09fa-4455-8e79-6198df95d78d">

## 문제점2

최근 2년간의 데이터를 가져오고 싶지만, 최대 6개월까지 가능.<br/>
링크를 임의로 조작해도 최대 6개월만 가능<br/>
따라서 6개월치씩 분류해서 가져올 예정<br/>
ex) 2022 상반기 부터 가져오고 싶다 -> 20220101~현재 이런식으로 가져오게 됨. 원하는 날짜부터 가져오게 하는 기능은 업데이트 하지 않을 예정(왜냐면 내가 필요 없음)<br/>

## 문제점3
utf - 8 인코딩 방식이 아님. 따라서 검색어를 '한국은행' 이라고 쳤을 시, utf-8로 인코딩 하는 것이 아닌, euc-kr로 인코딩 해야 함.<br/>


<img width="833" alt="image" src="https://github.com/junghwa0609/HI_IM_JUNGHWA/assets/161556739/8fa8ca66-d4f9-4dc1-a8f4-d18f40f4fcb7">

이렇게 더보기 버튼이 있고, 1페이지만 뜸 (더보기를 누르면 2페이지, 3페이지 이런식으로 넘어간다)<br/>

<img width="236" alt="image" src="https://github.com/junghwa0609/HI_IM_JUNGHWA/assets/161556739/5e61fc51-a946-460a-a968-866f8b30eb20">

이렇게 페이지 숫자를 검사를 누르든, 링크복사를 누르든 , 새탭에서 열기를 해보든 해서<br/>
페이지 링크를 새로 열면, 입찰 공고만 따로 나오는 창이 생긴다.<br/>
<br/>
URL을 복사해서 분석해 보았다.<br/>

https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?area=&areaNm=&bidNm=&bidSearchType=1&budgetCompare=&detailPrdnm=&detailPrdnmNo=&downBudget=&fromBidDt=2024%2F01%2F02&fromOpenBidDt=&industry=&industryCd=&instNm=%C7%D1%B1%B9%C0%BA%C7%E0&instSearchRangeType=&intbidYn=&maxPageViewNoByWshan=2&orgArea=&procmntReqNo=&radOrgan=1&recordCountPerPage=30&refNo=&regYn=Y&searchDtType=1&searchType=1&setMonth1=3&strArea=&taskClCds=&toBidDt=2024%2F07%2F04&toOpenBidDt=&upBudget=&currentPageNo=1

fromBidDt=2024%2F01%2F02: 입찰 시작 날짜 (2024/01/02).<br/>
toBidDt=2024%2F07%2F04: 입찰 종료 날짜 (2024/07/04).<br/>
instNm=%C7%D1%B1%B9%C0%BA%C7%E0: 기관명 (한국은행).<br/>
maxPageViewNoByWshan=2: 페이지 뷰 최대 수 (3). -- 임의로 조정 가능하다. 사실 아무 상관이 없다.<br/>
recordCountPerPage=30: 페이지 당 레코드 수 (100으로 할 것임). <br/>
currentPageNo=1: 현재 페이지 번호 (1).<br/>
<br/>
현재 페이지 번호가 페이지 뷰 최대 수를 넘어가도 아무 상관이 없었다.<br/>
따라서 필자는 현재 페이지 번호를 1씩 증가시켜가는 함수를 통해, 크롤링을 진행할 것이다.<br/>
또한 아무것도 없는 페이지가 나오면, '검색 결과가 없습니다.'라는 문구가 뜨므로, 그 문구를 종결 지점으로 잡아 크롤링을 완성할 것<br/>

## 문제점 4

2024/07/05 - 확인해보니 while문이 year의 조건때문에 2023년에서 자꾸 종료되는것 확인. 그래서 while함수 전체적으로 고침
그리고 페이지 당 레코드 수가 많을수록 페이지를 넘기는 횟수가 줄어드므로 최대 레코드 수를 확인 후 페이지당 레코드 수 변경시킬 것.
100까지 되는것 확인함.
(100을 넘으면 테이블을 찾을 수 없다고 뜸)


이제 함수에 시작년도, '공공기관이름(검색어)', 상반기시작 or 하반기 시작 
을 넣으면 크롤해와준다.
ex)
scrape_until_end(2021, '전력거래소', '상반기시작')
