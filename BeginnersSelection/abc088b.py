n = int(input())
a = map(int, input().split())

a = sorted(a, reverse=True)
print(sum(a[::2]) - sum(a[1::2]))