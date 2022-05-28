def solve(A, n):
	res = 0
	for i in range(n - 2, -1 , -1):
		while A[i] >= A[i + 1] and A[i] > 0:
			A[i] //= 2
			res += 1
		
		if A[i] == A[i + 1]:
			return -1

	return res


tcs = int(input())
for tc in range(tcs):
	n = int(input())
	A = [int(n) for n in input().split()]
	res = solve(A, n)
	print(res)
# print(solve([3, 6, 5], 3)) # 2
# print(solve([2, 8, 7, 5], 4)) # 4
# print(solve([5, 3, 2, 1], 4)) # -1
# print(solve([1, 2, 3, 4, 5], 5)) # 0
# print(solve([8, 26, 4, 21, 10], 5)) # 11

'''
	2 8 7 5
	2 4 7 5
	2 4 3 5
	2 2 3 5
	1 2 3 5


'''
