import collections
tcs = int(input())
for tc in range(tcs):
    n = int(input())
    A = [int(n) for n in input().split()]

    cnt = collections.Counter(A)
    if cnt[2] % 2 == 0 and cnt[1] % 2 == 0:
        print('YES')
        continue

    if cnt[2] % 2 == 1:
        if cnt[1] < 2:
            print('NO')
            continue
        else:
            cnt[1] -= 2
            cnt[2] += 1
    
    if cnt[1] % 2:
        print('NO')
    else:
        print('YES')