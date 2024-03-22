import math

def binary_number():
  a=float(input("2진수의 자릿수를 예측할 숫자를 입력하세요: "))
  b=math.log2(a)
  c=math.ceil(b)
  print(a,"을 2진수로 나타내면",c, "자리입니다.")

binary_number()
