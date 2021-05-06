tcs = int(input())
for tc in range(tcs):
    n = int(input())
    s = input()
    seen = set()
    
    i = 0
    flag = True
    while i < n:
        c = s[i]
        if c in seen:
            flag = False
            break
        seen.add(c)
        j = i + 1
        while j < n and c == s[j]:
            j += 1
        i = j
        
    
    print('Yes' if flag else 'No')
    