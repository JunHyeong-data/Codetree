n = int(input())

tot = 0
a_count = 0

for _ in range(n):
    string = input()
    tot += len(string)

    if string[0] == 'a':
        a_count += 1

print(tot, a_count)