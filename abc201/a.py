a = list(map(int, input().split()))

a.sort()
ans = 'No'
if a[2]-a[1] == a[1]-a[0]:
    ans = 'Yes'
print(ans)