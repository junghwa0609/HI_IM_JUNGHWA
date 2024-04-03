# HTML 주의사항

<img width="900" alt="image" src="https://github.com/junghwa0609/HI_IM_JUNGHWA/assets/161556739/f2188a02-dece-4623-b8f4-51451df56486">

<img width="523" alt="image" src="https://github.com/junghwa0609/HI_IM_JUNGHWA/assets/161556739/809febce-ef93-4f38-b122-6d5f741c4c10">


# 인터넷과 웹
태초의 컴퓨터 = 문서작성, 복잡한 연산
but 이것만 가지고는 컴퓨터 활용 불가.
두 컴퓨터를 연결해보면 어떨까? -> 두 컴퓨터를 연결하는 네트워크 탄생.

이  네트워크를 묶어서 근거리 지역 네트워크 (Local Area Network = LAN) 탄생
범지구적으로 컴퓨터를 연결한거 - 인터넷(inter network)
인터넷 위에서 정보를 교환할 수 있는 환경 = world wide web = web

web상에서 정보를 주고받는 방법

정보를 요청하는 컴퓨터 - 클라이언트
정보를 제공하는 컴퓨터 - 서버
정보를 제공하는 컴퓨터가 요청을 너무 많이 받으면 서버가 터졌다고 한다

클라 : 프로그래머스.co.kr정보좀 주세요 = HTTP요청(request)
서버 : ㅇㅋㅇㅋ or 엥?요청이 이상한데요? = HTTP응답(response)
= 이 과정을 HTTP라고 한다.
Hypertext Transfer(통신) Protocol(약속, 규율)

HTTP를 직관적으로 이해하기
내가 택배 주문할 때 쓰는 정보랑 비슷.
받는 사람 이름 host
받는 사람 주소 resource
배송방법 method

택배 - 송장(보내는사람, 받는사람 ...), 내용물
HTTP - Head( " ) ,Body(정보)

헤드에 담긴 정보
get / HTTP 1.1
Host : www.프로그래머스.com
User-Agent(나) : Mozilla/5.0

바디에 담긴 정보
내용물..

웹 페이지는 HTML이라는 형식으로 되어있고,
웹 브라우저(크롬)는 우리가 HTTP요청을 보내고, 응답받은 HTML코드를 렌더링(눈에보이게)해주었다.

웹 브라우저의 역할을 파이썬으로 해보자!!
그럼 그 전에 HTML에 대해 알아야 한다.

HTTP (hypertext transfer protocol)
HTML (hypertext markup language)

우리가 원하는 내용이 HTML문서의 어디에 있지? 어떤 태그로 묶여있지? 를 관찰해야 한다.