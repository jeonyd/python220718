print(" 리스트 내장(임베딩, 컴프리헨션")
lst = list(range(1,11))
print([i**2 for i in lst if i>5])

print("---필터링---")
lst = [10,25,30]
# 다른 언어의 Null: None
iterL = filter(None, lst)
for item in iterL:
    print(item)

# 조건이 되는 함수 정의
def getBiggerThan20(i):
    return i>20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)