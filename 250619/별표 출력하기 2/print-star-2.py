N = int(input())

for i in range(N, 0, -1): # N부터 1까지 1씩 감소하며 반복
    # 각 줄에 i개의 별표를 ' *' 형태로 붙여서 출력 (첫 별표는 공백 없음)
    # join을 사용하여 리스트의 요소들을 ' ' (공백)으로 연결
    print(' '.join(['*' for _ in range(i)]))