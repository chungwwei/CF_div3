tcs = int(input())
for _ in range(tcs):
	string = input()
	
	n = len(string)
	compare = 'abc'
	cnt = 0
	for i in range(n):
		if string[i] != compare[i]:
			cnt += 1
	
	if cnt > 2:
		print("NO")
	else:
		print("YES")
		
		
	
