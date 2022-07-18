

def solve(A, n):
	s = set()
	res = 0
	for i, problem in enumerate(A):
		if problem in s:
			res += 1
		else:
			res += 2
			s.add(problem)
	return res

tcs = int(input())
for tc in range(tcs):
	n = int(input())
	A = input()
	res = solve(A, n)
	print(res)




