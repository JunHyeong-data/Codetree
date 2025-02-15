arr = input().split()
a, b = int(arr[0]), int(arr[1])

for i in range(2, 9): 
    if i % 2 == 1:  # 홀수 단은 건너뛰기
        continue

    for j in range(b, a - 1, -1): 
        print(f'{j} * {i} = {j * i}', end='')
        if j != a:  
            print(' / ', end='')

    print()  # 줄바꿈
