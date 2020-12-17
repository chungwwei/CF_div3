tcs = int(input())
for tc in range(tcs):
    n = int(input())
    A = [int(n) for n in input().split()]
    left, right = 0, n - 1
    res = [0] * n
    i = 0
    for i in range(n):
        if i % 2 == 0:
            res[i] = str(A[left])
            left += 1
        else:
            res[i] = str(A[right])
            right -= 1

    print(' '.join(res))
        
