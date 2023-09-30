tcs = int(input())
for _ in range(tcs):
	n, X = list(map(int, input().split()))
	arr = list(map(int, input().split()))
 
	lo, hi = 1, 10 ** 9 + 1
	while lo <= hi:
		mid = lo + (hi - lo) // 2
		sumall = 0
		for i in range(n):
			sumall += (arr[i] + 2 * mid) ** 2
			if sumall > X:
				break
		if sumall == X:
			print(mid)
			break
		if sumall > X:
			hi = mid - 1
		else:
			lo = mid + 1
 
		