tcs = int(input())
for tc in range(tcs):
    n = int(input())
    A = [int(n) for n in input().split()]

    A.sort(reverse=True)
    score = 0
    for i in range(n):
        if i % 2 == 0:
            if A[i] % 2 == 0:
                score += A[i]
        else:
            if A[i] % 2 == 1:
                score -= A[i]
    
    if score > 0:
        print('Alice')
    elif score < 0:
        print('Bob')
    else:
        print('Tie')


        