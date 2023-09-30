tcs = int(input())
for _ in range(tcs):
	arr = list(map(int, input().split()))
	arr.sort()

	if arr[-1] + arr[-2] < 10:
		print("NO")
	else:
		print("YES")
		
		
	
