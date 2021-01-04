tcs = int(input())
for tc in range(tcs):
    n = int(input())
    A = [int(n) for n in input().split()]

    mx = 0
    dp = [n for n in A]
    for i in range(n - 1, -1, -1):
        if i + A[i] >= n:
            mx = max(mx, dp[i])
            continue
        dp[i] = dp[i + A[i]] + dp[i]
        mx = max(mx, dp[i])

    print(mx)

