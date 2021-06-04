a, b, c, x, y = map(int, input().split())

ans = a*x + b*y
ans = min(ans, c*max(x, y)*2)
if x > y:
    ans = min(ans, c*y*2+a*(x-y))
else:
    ans = min(ans, c*x*2+b*(y-x))
print(ans)