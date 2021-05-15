N, D, H = map(int, input().split())
high = 0.0

for i in range(N):
    d, h = map(int, input().split())
    high = max((-(H-h)/(D-d)*d + h), high)
print(high)