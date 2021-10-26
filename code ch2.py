inStr=input("문자를 입력 :")
outStr=""

for i in inStr:
    if i.isdigit():
        continue
    outStr += i

print("숫자 제거 --> " + outStr)
