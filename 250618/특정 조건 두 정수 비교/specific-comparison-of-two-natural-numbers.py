# 두 정수 A, B를 공백으로 구분하여 입력받습니다.
A, B = map(int, input().split())

# 첫 번째 수가 더 작은지 확인하고 결과를 is_A_smaller에 저장합니다.
is_A_smaller = 1 if A < B else 0

# 두 개의 수가 같은지 확인하고 결과를 are_A_B_equal에 저장합니다.
are_A_B_equal = 1 if A == B else 0

# 결과 값 두 개를 공백을 사이에 두고 출력합니다.
print(is_A_smaller, are_A_B_equal)