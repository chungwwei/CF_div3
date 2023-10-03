tcs = int(input())
for _ in range(tcs):
	n = int(input())
	string = input()

	i, j = 0, n - 1
	while i < j:
		if string[i] == '0' and string [j] == '1':
			i += 1
			j -= 1
		elif string[i] == '1' and string[j] == '0':
			i += 1
			j -= 1
		else:
			break
	
	print(j - i + 1)
	


		
		
	
