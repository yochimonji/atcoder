n, k = map(int, input().split())

inputs = {}
for i in range(n):
    a, b = map(int, input().split())
    if a in inputs.keys():
        inputs[a] += b
    else:
        inputs[a] = b
inputs = sorted(inputs.items())

ans = 0
for i,(a,b) in enumerate(inputs):
    if i==0:
        d = a
    else:
        d = inputs[i][0] - inputs[i-1][0]

    if k < d:
        break
    k = k - d + b
    ans += d
ans += k
print(ans)