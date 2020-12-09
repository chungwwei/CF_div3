t = int(input())
for k in range(t):
    n = int(input())

    res = []
    for i in range(n, 0, -1):
        res.append(i)
    
    if len(res) % 2 == 1:
        mid = len(res) // 2
        temp = res[mid]
        res[mid] = res[mid - 1]
        res[mid - 1] = temp
    

    res = map(str, res)
    print(' '.join(res))