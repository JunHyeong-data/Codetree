arr = []

for _ in range(4):
    word = input()
    arr.append(word)

for elem in arr[::-1]:
    print(elem)