# 자연수 Y를 입력받습니다.
Y = int(input())

# 윤년인지 판단하는 조건:
# 1. 4로 나누어 떨어지는 해는 윤년 (Y % 4 == 0)
# 2. 단, 예외적으로 100으로 나누어 떨어지지만 400으로 나누어 떨어지지 않는 해는 평년으로 합니다.
#    즉, (Y % 100 == 0) and (Y % 400 != 0) 인 경우는 윤년이 아닙니다.

is_leap_year = False

if Y % 4 == 0:
    if Y % 100 == 0:
        if Y % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False # 100으로 나누어 떨어지지만 400으로 나누어 떨어지지 않으면 평년
    else:
        is_leap_year = True # 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년
else:
    is_leap_year = False # 4로 나누어 떨어지지 않으면 평년

# 결과 출력
if is_leap_year:
    print("true")
else:
    print("false")