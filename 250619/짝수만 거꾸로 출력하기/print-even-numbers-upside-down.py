# 첫 줄에 N의 정수가 주어집니다.
N = int(input())

# N개의 정수가 차례대로 공백으로 구분되어 주어집니다.
numbers = list(map(int, input().split()))

# 짝수만 저장할 리스트를 선언합니다.
even_numbers = []

# 주어진 정수 중에서 짝수를 찾아서 even_numbers 리스트에 추가합니다.
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# even_numbers 리스트를 역순으로 정렬합니다.
even_numbers.reverse()

# 역순으로 정렬된 짝수들을 공백으로 구분하여 출력합니다.
print(*even_numbers)