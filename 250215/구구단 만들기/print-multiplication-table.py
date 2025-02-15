a, b = map(int, input().split())

for i in range(1, 10):

    cnt=0

    for j in range(b,a-1,-2):

        cnt+=1

        print(f"{j} * {i} = {i * j}",end="")

        if cnt <= (b-a) // 2:

            print(" / ",end="")

    print()