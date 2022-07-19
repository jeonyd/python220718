# function4.py

def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#가변인자 (입력 파라미터 개수가 가변적인 경우)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))

#정의되지 않은 인자 (앞에 두개 필수, 딕셔너리 옵션)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출

print(userURIBuilder("credu.com","80",id="kim",passwd="1234"))
print(userURIBuilder("credu.com","80",id="kim",passwd="1234",
    name = "mike"))

#람다함수
g = lambda x,y:x*y
print(g(3,4))
print((lambda x:x*x)(3))
print( globals())