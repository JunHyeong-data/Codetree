# N 입력 받기
n = int(input())

# N개의 문자열을 저장할 리스트
strings = []
for _ in range(n):
    strings.append(input())

# 비교할 문자 입력 받기
target_char = input()

# 개수와 길이의 합 초기화
count = 0
total_length = 0

# 리스트를 순회하며 조건에 맞는 문자열 찾기
for s in strings:
    if s.startswith(target_char): # s[0] == target_char와 동일
        count += 1
        total_length += len(s)

# 평균 계산
average = total_length / count

# 결과 출력 (소수점 자릿수 조절)
print(f'{count} {average:.2f}')