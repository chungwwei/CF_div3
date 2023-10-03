from collections import Counter
tcs = int(input())
for _ in range(tcs):
	n = int(input())
	string = input()
	arr = [n for n in string]

	cnt = Counter(arr)
	mx = len(cnt)
	left = Counter()
	for i in range(n):
		char = string[i]	
		mx = max(mx, len(cnt) + len(left))
		cnt[char] -= 1
		if cnt[char] == 0:
			del cnt[char]
		left[char] += 1
	print(mx)





		
		
	
