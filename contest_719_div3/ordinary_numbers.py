tcs = int(input())
for i in range(tcs):
    n = int(input())
    cnt = 0
    for d in range(1, 10):
        for length in range(1, 10):
            val = 0
            for i in range(length):
                val = val * 10 + d
            if val <= n: 
                cnt += 1
    print(cnt)
