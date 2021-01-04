def into_two(n):
    res = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
            res = 2 * res
        else:
            break
    return res

# print(into_two(12))
# print(into_two(8))
# print(into_two(4))
# print(into_two(16))
# print(into_two(20))
tcs = int(input())
for tc in range(tcs):
    A = [int(n) for n in input().split()]
    w, h, k = A[0], A[1], A[2]

    a = into_two(w)
    b = into_two(h)

    if a * b >= k:
        print('YES')
    else:
        print('NO')