arr = list(map(int, input().split()))

result = []
for elem in arr:
    if elem == 0:
        break
    else:
        result.append(elem)
sum_val = sum(result)
avg = sum_val / len(result)
print(f"{sum_val} {avg:.1f}")