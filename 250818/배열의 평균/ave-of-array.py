arr = [list(map(int, input().split())) for _ in range(2)]

row_avg = [sum(row) / len(row) for row in arr]
trans = zip(*arr)
col_avg = [sum(col) / len(col) for col in trans]

# 전체 숫자의 개수를 동적으로 계산
total_count = len(arr) * len(arr[0])

# 이중 sum() 함수를 사용한 간결한 합계 계산
total_sum = sum(sum(row) for row in arr)
total_avg = total_sum / total_count

# 소수점 첫째 자리까지 출력
print(' '.join([f'{avg:.1f}' for avg in row_avg]))
print(' '.join([f'{avg:.1f}' for avg in col_avg]))
print(f'{total_avg:.1f}')