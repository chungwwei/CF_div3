from collections import defaultdict
tcs = int(input())
for tc in range(tcs):
    n = int(input())
    A = [int(n) for n in input().split()]
    # a_j - a_i = j - i
    # a_j - j = a_i - i

    cnt = 0
    d = defaultdict(int)
    for i in range(n):
        cnt += d[A[i] - i]
        d[A[i] - i] += 1
    print(cnt)
