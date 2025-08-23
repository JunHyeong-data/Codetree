n = int(input())
arr = [input() for _ in range(n)]

total_sum = 0

for digit in arr:
    total_sum += int(digit)

result = str(total_sum)
print(result[1:]+result[0])