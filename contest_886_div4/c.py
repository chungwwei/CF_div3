tcs = int(input())
for _ in range(tcs):
	A = []
	first = None
	for i in range(8):
		string = input()
		A.append(list(string))
		for j in range(8):
			if string[j] != '.' and first == None:
				first = (i, j)
	
	start_row = first[0]
	column = first[1]
	res = []
	for k in range(start_row, 8):
		if A[k][column] != '.':
			res.append(A[k][column])
	print("".join(res))

