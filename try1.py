def divide(a,b):
    return a/b

#호출
try:
    result = divide(5,0)
    print("결과:{0".format(result))

except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다")
else:
    print("결과:{0".format(result))
finally:
    print("한번 더 체크")


print("----종료----")