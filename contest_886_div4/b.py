'''
3
5
7 2
12 5
9 3
9 4
10 1
3
1 2
3 4
5 6
1
1 43
'''

tcs = int(input())
for _ in range(tcs):
	n = int(input())
	arr = []
	for k in range(n):
		a, b = list(map(int, input().split()))
		if a <= 10:
			arr.append((b, a, k + 1))
	arr.sort()
	print(arr[-1][-1])
		
		
	
