
def solve(A):
	if len(A) != 3:
		return False
	A = A.lower()
	return A[0] == 'y' and A[1] == 'e' and A[2] == 's'
	

tcs = int(input())
for tc in range(tcs):
	A = input()
	res = solve(A)
	print("YES" if res else "NO")




