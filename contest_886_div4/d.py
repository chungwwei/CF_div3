tcs = int(input())
for _ in range(tcs):
	n, k = list(map(int, input().split()))
	arr = list(map(int, input().split()))

	if n == 1 and arr[0] > k:
		print('0')
		continue
	arr.sort()

	mx = 0
	i = 0
	while i < n:
		j = i + 1
		while j < n and abs(arr[j] - arr[j - 1]) <= k:
			mx = max(mx, j - i + 1)
			j += 1
		i = j
	
	print(n - mx)

'''
7
5 1
1 2 4 5 6
1 2
10
8 3
17 3 1 20 12 5 17 12
4 2
2 4 6 8
5 3
2 3 19 10 8
3 4
1 10 5
8 1
8 3 1 4 5 10 7 3
'''
	