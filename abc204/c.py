import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
c = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    c[a-1].append(b-1)

def dfs(v):
    if temp[v]:
        return
    temp[v] = True
    for i in c[v]:
        dfs(i)

ans = 0
for i in range(n):
    temp = [False]*n
    dfs(i)
    ans += sum(temp)
print(ans)