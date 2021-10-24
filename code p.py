def count(num):
    if num <= 1:
        return num
    else:
        return(count(num-1)) + (count(num-2))

F = int(input("피보나치 수열 F(N)의 N값을 입력하세요 --> "))

print("F(%d) = %d" % (F, count(F)))
