## 변수 선언 부분 ##
select, answer , numstr, num1, num2= 0,0, "", 0, 0

##메인 코드 부분##
select= int(input("1.입력한 수식 계산, 2.두 수 사이의 합계:"))

if select == 1:
    numstr= input("수식을 입력하세요:")
    answer= eval(numstr)
    print("%s 결과는 %5.1f입니다." % (numstr,answer))
elif select ==2:
    num1= int(input("첫번쨰 숫자를 입력하세요:"))
    num2= int(input("두번쨰 숫자를 입력하세요:"))
    for i in range(num1, num2+1):
        answer+=i
        print("%d+...+%d는 %d입니다."%(num1, num2, answer))
else:
    print("1 또는 2의 값만 입력해야 됩니다.")
    
    
