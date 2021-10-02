n = int(input())

li = []

for i in range(n):
    a, b = map(int, input().split())
    if len(li) < a+b-1:
        li = li + [0] * ((a+b-1) - len(li))
    for j in range(a-1, a+b-1):
        li[j] += 1
print(li)

result = [0] * n
for l in li:
    result[l] += 1
print(' '.join(map(str, result)))