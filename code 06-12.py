hap=0
a,b=0,0

while True:
    a=int(input("더할 첫번째 숫자를 입력하세요:"))
    if a==0:
        break
    b=int(input("더할 두번째 숫자를 입력하세요:"))
    hap=a+b
    print("%d+%d=%d"%(a,b,hap))

print("0을 입력해 반복문을 탈출했습니다.")

