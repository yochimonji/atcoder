import collections

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = []
for i in range(n):
    d.append(b[c[i]-1])

ans = 0
a_count = collections.Counter(a)
d_count = collections.Counter(d)
for key in a_count:
    ans += a_count[key] * d_count[key]
print(ans)