tcs = int(input())
for tc in range(tcs):
    n = int(input())
    A = input()
    TARGET = '2020'
    flag = False
    for left in range(0, 5):
        right = 4 - left
        if A[:left] + A[n - right:] == TARGET:
            print('YES')
            flag = True
            break
    
    if not flag:
        print('NO')
    