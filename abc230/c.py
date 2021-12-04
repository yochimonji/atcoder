n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

max_n = max(1-a, 1-b)
min_n = min(n-a, n-b)

ans = [['.']*(s-r+1)]*(q-p+1)

for i in range(q-p+1):
    for j in range(s-r+1):
        for k in range(max_n, min_n+1):
            if i+1==a+k and (j+1==b+k or j+1==b-k):
                ans[i-1][j-1] = '*'
                break
            else:
                break
for i in ans:
    print(''.join(i))