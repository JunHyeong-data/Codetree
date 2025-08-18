arr = [list(input().split()) for _ in range(5)]

for elem in arr:
    for j in elem:
        print(j.upper(), end=' ') 
    print()