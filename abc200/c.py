import collections, math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] % 200
c = collections.Counter(a)

ans = 0
for i in c.values():
    if i >= 2:
        ans += combinations_count(i, 2)
print(ans)