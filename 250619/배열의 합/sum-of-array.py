for _ in range(4): # 4줄의 입력을 처리
    numbers = list(map(int, input().split())) # 한 줄의 4개 정수를 리스트로 변환
    row_sum = sum(numbers) # 해당 줄의 모든 숫자를 합산
    print(row_sum) # 합계 출력