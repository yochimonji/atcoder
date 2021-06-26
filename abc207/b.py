import math

a, b, c, d = map(int, input().split())

if b >= c*d:
    print(-1)
    exit()

ans = math.ceil(a/(c*d-b))
print(ans)