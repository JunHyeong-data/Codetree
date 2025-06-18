# 첫 번째 줄에 원소의 개수를 나타내는 N이 주어집니다.
N = int(input())

# 두 번째 줄에는 N개의 원소가 공백을 사이에 두고 주어집니다.
elements = list(map(int, input().split()))

# 각 원소를 제곱한 결과를 저장할 리스트를 생성합니다.
squared_elements = []

# 각 원소에 대해 제곱을 수행하고 새 리스트에 추가합니다.
for element in elements:
    squared_elements.append(element ** 2)

# 제곱한 결과들을 공백을 사이에 두고 입력받은 순서대로 출력합니다.
print(*squared_elements) # * 연산자를 사용하여 리스트의 요소들을 개별 인자로 전달하여 출력합니다.