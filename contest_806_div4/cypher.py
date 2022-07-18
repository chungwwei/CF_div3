def solve(W, A, rolls):
	res = [0] * W
	for i, (sz, lst) in enumerate(rolls):
		for action in lst:
			if action == 'D':
				A[i] += 1
				A[i] %= 10
			else:
				A[i] -= 1
				A[i] %= 10
	return A


tcs = int(input())
for tc in range(tcs):
	W = int(input())
	A = [int(n) for n in input().split()]
	rolls = []
	for _ in range(W):
		line = input().split()
		rolls.append((line[0], line[1]))
	res = solve(W, A, rolls)
	print(" ".join(str(n) for n in res))




