import re

result = re.search("[0-9]*th","  35th")
print(result)
print(result.group())

result = re.match("[0-9]*th","35th")  #완벽하게 일치해야 함
print(result)
print(result.group())

print(bool(re.search("apple","this is apple")))
print(bool(re.match("apple","this is apple")))