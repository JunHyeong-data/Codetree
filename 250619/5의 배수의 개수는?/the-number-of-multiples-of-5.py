count_of_multiples_of_5 = 0

for _ in range(4): # 4행을 읽음
    row = list(map(int, input().split())) # 한 행의 정수들을 리스트로 변환
    for num in row: # 해당 행의 각 숫자에 대해 반복
        if num % 5 == 0: # 5의 배수인지 확인
            count_of_multiples_of_5 += 1

print(count_of_multiples_of_5)