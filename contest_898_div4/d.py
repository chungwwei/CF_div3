tcs = int(input())
for _ in range(tcs):
	n, k = list(map(int, input().split()))
	arr = input()

	i = 0
	cnt = 0
	while i < n:
		if arr[i] == "W":
			i += 1
			continue
		else:
			cnt += 1
			i += k

	print(cnt)
		
