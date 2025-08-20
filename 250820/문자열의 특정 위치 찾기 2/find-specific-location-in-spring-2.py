words = ['apple', 'banana', 'grape', 'blueberry', 'orange']
target = input()

count = 0
for words in words:
    if words[2] == target or words[3] == target:
        print(words)
        count += 1

print(count)
