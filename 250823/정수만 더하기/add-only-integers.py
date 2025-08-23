s = input()
total = 0

for char in s:
    if char.isdigit():
        total += int(char)

print(total)