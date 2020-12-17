tcs = int(input())
for tc in range(tcs):
    n = int(input())
    d = 9
    if n > 45:
        print(-1)
        continue
    res = []
    while n > 0:
        val = min(d, n)
        res.append(str(val))
        n -= d
        d -= 1
    res = reversed(res)
    print(''.join(res))

