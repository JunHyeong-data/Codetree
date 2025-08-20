input_string = input()
target = input()

cnt = 0
for elem in input_string:
    if elem == target:
        cnt += 1

print(cnt)