import collections
t = int(input())
for k in range(t):
    n = int(input())
    arr = [int(n) for n in input().split()]

    cnt = collections.Counter(arr)
    lst = []
    for k, v in cnt.items():
        if v == 1:
            lst.append(k)
    if not lst:
        print(-1)
        continue
    mn = min(lst)
    pos = -1
    for i in range(len(arr)):
        if arr[i] == mn:
            pos = i
    print(pos + 1)
    