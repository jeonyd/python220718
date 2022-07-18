# function1.py

def times(a,b):
    return a+b, a*b


# 함수 호출
result = times(3,4)
print(result)

# 함수 정의
def setValue(newValue):
    x=  newValue
    print("함수 내부:", x)

# 호출
print(setValue(5))

#교집합을 리턴
def intersect(prelist,postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result
#호출
print(intersect("HAM","SPAM"))