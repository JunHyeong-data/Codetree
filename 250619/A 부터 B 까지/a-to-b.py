A, B = map(int, input().split())

results = []
current_num = A

while current_num <= B:
    results.append(str(current_num)) # 현재 숫자를 결과 리스트에 추가

    if current_num % 2 == 1: # 홀수인 경우
        current_num *= 2
    else: # 짝수인 경우
        current_num += 3

print(" ".join(results))