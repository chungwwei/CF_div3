tcs = int(input())
for _ in range(tcs):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()

	arr[0] += 1
	p = 1
	for i in range(n):
		p *= arr[i]
	
	print(p)
