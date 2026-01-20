# 네이버 메인 페이지의 title 가져오기

#1. 웹 페이지 요청을 보내기 위한 라이브러리
import requests

#2. html을 분석(파싱) 하기 위한 라이브러리
from bs4 import BeautifulSoup

#3. 크롤링 할 웹 페이지 주소

url= 'https://www.naver.com'

#4. 해당 url로 Get 요청을 보내고 응답을 받음
response= requests.get(url)

#5. 서버 응답이 정상인지 확인 (200 이면 성공)
print(response.status_code)

#6. 받아온 HTML내용을 Beautifulsoup 객체로 변환
# 'html_parser'는 파이썬 기본 HTML 분석기
soup = BeautifulSoup(response.text,'html.parser')

# 7. HTML 문서의 <title>태그를 찾음
title = soup.title

# 8. title 태그 안의 텍스트만 출력
print(title.text)
