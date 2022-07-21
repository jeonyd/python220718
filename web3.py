#web2.py
#  네이버 웹툰 페이지 별 받아오기

#웹서버와 통신할 경우
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#파일로 저장
f = open("webtoon.txt","wt",encoding="utf-8")

#페이지 처리를 위해 range함수 사용
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)

    #네이버에서 실행한 페이지결과를 문자열로 받기
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체
    soup = BeautifulSoup(data,"html.parser")
    #특정한 태그를 검색
    cartoons = soup.find_all("td", class_="title")


    for item in cartoons:
        item2 = item.find("a")
        title = item2.text.strip()
        print(title)
        f.write(title + "\n" )

f.close()
print("웹 크롤링 종료")