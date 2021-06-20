import collections

n = int(input())
a = list(map(int, input().split()))

total = (n * (n-1)) // 2
a_count = collections.Counter(a)

for val in a_count.values():
    if val != 1:
        total -= (val * (val-1)) // 2
print(total)