n = int(input())

ans = 0
for i in range(n):
    if len(str(i+1))%2 == 1:
        ans += 1
print(ans)