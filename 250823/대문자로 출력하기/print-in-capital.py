s = input()

s = s.upper()

for elem in s:
    if ord(elem) >= ord('A') and ord(elem) <= ord('Z'):
        print(elem, end='')