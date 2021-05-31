a, b, c = map(int, input().split())

ans = 0
if a==b:
    ans = c
if b==c:
    ans = a
if a==c:
    ans = b
print(ans)