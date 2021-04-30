a = int(input()) + 1  # 500yen
b = int(input()) + 1  # 100yen
c = int(input()) + 1  # 50yen
x = int(input())  # target_value
ans = 0

for ai in range(a):
    for bi in range(b):
        for ci in range(c):
            if 500*ai + 100*bi + 50*ci == x:
                ans += 1

print(ans)