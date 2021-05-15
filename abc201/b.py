n = int(input())
ans = dict()

for i in range(n):
    inputs = input().split()
    ans[inputs[0]] = int(inputs[1])
print(sorted(ans.items(), key=lambda x:x[1])[-2][0])