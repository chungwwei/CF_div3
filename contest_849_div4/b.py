tcs = int(input())
for _ in range(tcs):
	n = int(input())
	directions = input()
	flag = False
	pos = [0, 0]
	for i in range(n):
		d = directions[i]
		if d == 'U':
			pos[1] += 1
		elif d == 'D':
			pos[1] -= 1
		elif d == 'L':
			pos[0] -= 1
		elif d == 'R':
			pos[0] += 1
		
		if pos[0] == 1 and pos[1] == 1:
			flag = True
			break
	if flag:
		print("YES")
	else:
		print("NO")

		
		
	
