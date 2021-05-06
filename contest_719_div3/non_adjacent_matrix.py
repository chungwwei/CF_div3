tcs = int(input())
for tc in range(tcs):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(-1)
        continue

    M = [[0] * n for _ in range(n)]
    odd = 1
    even = 2
    for i in range(n):
        for j in range(n):
            if odd <= n * n:
                M[i][j] = str(odd)
                odd += 2
            else:
                M[i][j] = str(even)
                even += 2
    for lst in M:
        print(' '.join(lst))
