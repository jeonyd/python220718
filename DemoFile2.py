#DemoFile2.py

#파일 생성
f= open("demo.txt","wt")
f.write("첫번째\n두번째")
f.close()

#파일을 읽어서처리
f = open("demo.txt","rt")
result = f.read()
print(result)
print(f.tell())
f.seek(0) #처음으로 가는 거
lst = f.readlines()
print(lst)

#처음으로 리셋
f.seek(0)
print(f.readline())
print(f.readline())
f.close()

#with구문
with open("demo.txt","rt") as f:
    for item in f.readlines():
        print(item, end="")

print("---첨부하는 경우---")
#wt, a+ 다른 상황
f = open("demo.txt","a+")
f.write("다른 데이터\n")
f.close