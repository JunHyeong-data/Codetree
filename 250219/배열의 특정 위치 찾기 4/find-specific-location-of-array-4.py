arr = list(map(int, input().split()))

result = []
for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 0:
        result.append(elem)
sum_val = sum(result)
length = len(result)
print(f"{length} {sum_val}")