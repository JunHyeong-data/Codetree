s1 = input()
s2 = input()
s3 = input()

l1 = len(s1)
l2 = len(s2)
l3 = len(s3)

max_len = max(l1,l2,l3)
min_len = min(l1,l2,l3)

print(max_len-min_len)