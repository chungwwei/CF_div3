tcs = int(input())
for _ in range(tcs):
	n, K = list(map(int, input().split()))
	fruits = list(map(int, input().split()))
	heights = list(map(int, input().split()))

	prefix = [0] * (n + 1)
	for i in range(n):
		prefix[i + 1] = prefix[i] + fruits[i]

	lengths = [0] * (n)
	lengths[n - 1] = 1
	for i in range(n - 2, -1, -1):
		if heights[i] % heights[i + 1] == 0:
			lengths[i] = lengths[i + 1] + 1
		else:
			lengths[i] = 1
	
	print(lengths)
	def check(dist):
		found = False
		for i in range(0, n - dist + 1):
			if lengths[i] < dist:
				continue
			total = prefix[i + dist] - prefix[i]
			if total <= K:
				found = True
				break
		return found
		
	lo, hi = 1, n
	while lo <= hi:
		mid = (lo + hi) // 2
		if check(mid):
			lo = mid + 1
		else:
			hi = mid - 1
	
	print(hi)


'''
1
5 12
3 2 4 1 8
4 4 2 4 1
'''