#DemoFile.py

#파일 생성
f= open("demo.txt","wt")
f.write("첫번째\n두번째")
f.close()

#파일을 읽어서처리
f = open("demo.txt","rt")
result = f.read()
print(result)
f.close()