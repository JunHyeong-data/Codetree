arr = list(map(int, input().split()))

result = []
for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 0:
        result.append(elem)
sum_val = sum(result)
avg = sum_val / len(result)
print(f"{len(result)} {sum_val}")