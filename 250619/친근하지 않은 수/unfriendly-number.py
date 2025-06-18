# 정수 N을 입력받습니다.
N = int(input())

# 친근하지 않은 수의 개수를 세기 위한 카운터
unfriendly_count = 0

# 1부터 N까지의 모든 정수를 확인합니다.
for i in range(1, N + 1):
    # 친근한 수의 조건: 2, 3 또는 5로 나누어 떨어지는 수
    # 즉, i % 2 == 0 or i % 3 == 0 or i % 5 == 0 인 경우
    
    # 친근하지 않은 수의 조건: 2, 3, 5 그 어떤 수로도 나누어 떨어지지 않는 수
    # 즉, not (i % 2 == 0 or i % 3 == 0 or i % 5 == 0)
    # 이는 (i % 2 != 0 and i % 3 != 0 and i % 5 != 0) 과 동일합니다.
    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0):
        unfriendly_count += 1

# 친근하지 않은 수의 개수를 출력합니다.
print(unfriendly_count)