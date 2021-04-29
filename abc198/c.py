import math

r, x, y = map(float, input().split())
d = math.sqrt(x*x + y*y)

if r == d:
    print(1)
elif 2*r >= d:
    print(2)
else:
    print(math.ceil(d/r))