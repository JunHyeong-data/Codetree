# 3개의 정수 A, B, C를 공백으로 구분하여 입력받습니다.
# 중앙값을 찾기 위해 리스트에 저장하고 정렬하는 것이 가장 효율적입니다.
numbers = list(map(int, input().split()))

# 리스트를 오름차순으로 정렬합니다.
numbers.sort()

# 정렬된 리스트의 중간 값(인덱스 1)이 중앙값입니다.
print(numbers[1])