n = int(input())
A = map(int, input().split())

ans = 0
for a in A:
    if a > 10:
        ans += a - 10
print(ans)