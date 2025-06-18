# 정수 a를 입력받습니다.
a = int(input())

# a가 13의 배수이거나 19의 배수인 경우 True, 그 외의 경우 False를 출력합니다.
if (a % 13 == 0) or (a % 19 == 0):
    print("True")
else:
    print("False")