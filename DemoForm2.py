# DemoForm.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)

import sys
from PyQt5. QtWidgets import *
from PyQt5 import uic

#웹서버와 통신할 경우
import urllib.request
#크롤링
from bs4 import BeautifulSoup


# 폼디자인을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class): #창 여러개 띄워서 왔다갔다 하는 건 QMainWindow 메뉴툴바 등등  <->간단한건 QDialog
    #초기화 매서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    #슬롯 메서드
    def firstClick(self):

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
        self.label.setText("웹툰 크롤링 종료")


    
    def secondClick(self):
        self.label.setText("두번째 클릭")
        
    def thirdClick(self):
        self.label.setText("세번째 클릭")


# 진입점을 체크
if __name__== "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()