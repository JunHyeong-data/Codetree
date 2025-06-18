# 자연수 N을 입력받습니다.
N = int(input())

# N이 "굉장한 수"인지 판단합니다.
# 굉장한 수는 다음 두 조건 중 하나를 만족해야 합니다.
# 1. 홀수이면서 3의 배수인 수
# 2. 짝수이면서 5의 배수인 수

# 첫 번째 조건: N이 홀수 (N % 2 != 0) 이면서 3의 배수 (N % 3 == 0)
condition1 = (N % 2 != 0) and (N % 3 == 0)

# 두 번째 조건: N이 짝수 (N % 2 == 0) 이면서 5의 배수 (N % 5 == 0)
condition2 = (N % 2 == 0) and (N % 5 == 0)

# 두 조건 중 하나라도 만족하면 "true", 그렇지 않으면 "false" 출력
if condition1 or condition2:
    print("true")
else:
    print("false")