input_str = input()
target_str = input()

# Please write your code here.
result = -1

for i in range(len(input_str)):
    if input_str[i:i+len(target_str)] ==  target_str:
        result = i
        break

print(result)