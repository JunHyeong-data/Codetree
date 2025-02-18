arr = list(map(int, input().split()))
sum_val = 0
result = []
for elem in arr[1:10:2]:
    sum_val += elem
for love in arr[2:10:3]:
    result.append(love)
avg = sum(result) / len(result)
print(f"{sum_val} {avg:.1f}")
    
