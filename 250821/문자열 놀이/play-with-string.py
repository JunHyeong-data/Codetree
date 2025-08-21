s, q = input().split()
q = int(q)

for _ in range(q):
    query = input().split()
    query_type = query[0]

    if query_type == '1':
        a = int(query[1])
        b = int(query[2])

        s_list = list(s)
        s_list[a-1], s_list[b-1] = s_list[b-1], s_list[a-1]
        s = "".join(s_list)
        print(s)
    
    elif query_type:
        x = query[1]
        y = query[2]

        s = s.replace(x, y)
        print(s)