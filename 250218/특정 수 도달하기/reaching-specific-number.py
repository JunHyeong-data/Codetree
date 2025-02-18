arr = list(map(int, input().split()))
me = []
for elem in arr:
    if elem < 250:
        me.append(elem)
    else:
        break
sum_val = sum(me)
print(sum_val,end=' ')
print(f"{sum_val/len(me):.1f}")
    

