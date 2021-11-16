  print("나누기 전용 계산기 입니다.")

   nums = []

   nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))

   nums.append(int(input("두 번째 숫자를 입력하세요 : ")))

   nums.append(int(nums[0] / nums[1]))

   print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:

   print("에러! 잘못된 값을 입력 하였습니다.")

except ZeroDivisionError as err:

   print(err)

except Exception as err:

   print("알 수 없는 에러가 발생하였습니다.")

   print(err)
[출처] [Python]파이썬 코딩 기본편 ㅣ 10-1 예외 처리, 10-2 에러 발생 시키기|작성자 뽀홀릭
