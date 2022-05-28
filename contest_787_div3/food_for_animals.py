def solve(a, b, c, x, y):
	x -= min(a, x)
	y -= min(b, y)
	return c >= x + y


tcs = int(input())
for tc in range(tcs):
	A = [int(n) for n in input().split()]
	a, b, c, x, y = A
	res = solve(a, b, c, x, y)
	print("YES" if res else "NO")






