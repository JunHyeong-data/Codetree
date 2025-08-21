A = input()
encoded_string = ""
# Please write your code here.
cnt = 1
if not A:
    print(0)
else:
    for i in range(len(A)):
        if i == len(A) - 1 or A[i] != A[i+1]:
            encoded_string += A[i] + str(cnt)
            cnt = 1
        else:
            cnt += 1
print(len(encoded_string))
print(encoded_string)
        
