a, b, k = map(int, input().split())
ans = []
for i in range(100):
    if a%(i+1)==0 and b%(i+1)==0:
        ans.append(i+1)
print(ans[-k])