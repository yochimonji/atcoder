n = int(input())
a = map(int, input().split())
b = map(int, input().split())

a_max = max(a)
b_min = min(b)

val = b_min - a_max + 1
if val < 0:
    print(0)
else:
    print(val)