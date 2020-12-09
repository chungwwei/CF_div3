import collections
t = int(input())
for k in range(t):
    n = int(input())
    A = [int(n) for n in input().split()]

    if n == 1:
        print(0)
        continue
    B = []
    for i in range(len(A)):
        if i == 0:
            B.append(A[i])
        else:
            if A[i] != B[-1]:
                B.append(A[i])
    
    cnt = collections.Counter(B)
    first, last = B[0], B[-1]
    for k, v in cnt.items():
        cnt[k] += 1
        if k == first:
            cnt[k] -= 1
        if k == last:
            cnt[k] -= 1
    print(min(cnt.values())) 

    
    