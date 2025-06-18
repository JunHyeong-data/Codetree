def is_prime(n):
    """소수 판별 함수"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start, end = map(int, input().split())

count = 0
for num in range(start, end + 1):
    # 어떤 수의 제곱근이 정수이고, 그 제곱근이 소수인지 확인
    sqrt_num = int(num**0.5)
    if sqrt_num * sqrt_num == num:  # num이 어떤 정수의 제곱수인지 확인
        if is_prime(sqrt_num):  # 그 정수가 소수인지 확인
            count += 1

print(count)