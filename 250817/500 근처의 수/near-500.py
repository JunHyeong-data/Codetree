arr = list(map(int, input().split()))

num1 = -1
num2 = 1001

for i in range(len(arr)):
    if arr[i] < 500 and arr[i] > num1:
        num1 = arr[i]
for j in range(len(arr)):
    if arr[j] > 500 and arr[j] < num2:
        num2 = arr[j]
print(num1, num2)

