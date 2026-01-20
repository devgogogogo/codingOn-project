import requests
from bs4 import BeautifulSoup
import json

# 뉴스 검색 URL
url = 'https://search.naver.com/search.naver?where=news&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'

# 나는 봇이 아니라 브라우져다 라고 속이기
# 네이버는 User_Agent 없으면 차단함
#최소 이 한줄은 필수!! 입니다.
headers = {
    "User-Agent": "Mozilla/5.0"

}

#실제로 네이버 서버에 요청을 보냄
# 브라우저에서 주소 누른 것과 같음
# 결과물 response 객체에 담음

response = requests.get(url,headers=headers)

#서버가 보내준 HTML  전체 코드
html = response.text

#HTML 문자열을 분석 가능한 구조로 변환
# 이 상태가 되면 태그 <a>, <div>등을 검색 할 수 있음
soup = BeautifulSoup(html,"html-parser")

# a 태그 중 href 있는 것 전부 찾기
links = soup.find_all("a",href=True)

# 갯수 확인용
count =0


# links 에서 찾은 것들 반복문
for a in links:
    
    # a태그의 href 속성 값 가져오기
    href = a["href"].strip()
    
    #a 태그 안에 들어 있는 글자 전부 가져오기
    # strip =True는 줄 바꿈, 공백 제거 입니다.
    title = a.get_text(strip=True)

    # title이 빈 문자열이 아니여야 하고 외부 실제 기사링크 여야 하고 뉴스 기사 URL패턴 필터링
    if (title and href.startswith("https://")and "view" in href):
        count +=1
        print(f"{count}. {title}")
        print(f"  {href}")
print("총 뉴스 개수: ", count)    
   


