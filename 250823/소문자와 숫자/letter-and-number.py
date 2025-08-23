s = input()
result = ''

for char in s:
    ascii_code = ord(char)
    if ord('a') <= ascii_code <= ord('z'):
        result += char
    if ord('A') <= ascii_code <= ord('Z'):
        result += char
    # Check if the character is a number
    elif ord('0') <= ascii_code <= ord('9'):
        result += char

print(result.lower())