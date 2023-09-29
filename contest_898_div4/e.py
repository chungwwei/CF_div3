tcs = int(input())
for _ in range(tcs):
	n, X = list(map(int, input().split()))
	arr = list(map(int, input().split()))

	lo, hi = 0, 20 ** 9
	while lo < hi:
		mid = lo + (hi - lo + 1) // 2
		waters = 0
		for i in range(n):
			if mid > arr[i]:
				waters += max(0, mid - arr[i])

		if waters <= X:
			lo = mid
		else:
			hi = mid - 1

	print(lo)

		
