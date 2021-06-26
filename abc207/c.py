n = int(input())
li = []
for i in range(n):
    t, l, r = map(int, input().split())
    if t==1:
        li.append([l, r])
    elif t==2:
        li.append([l, r-0.1])
    elif t==3:
        li.append([l+0.1, r])
    else:
        li.append([l+0.1, r-0.1])

ans = 0
for i in range(len(li)-1):
    for j in range(i+1, len(li)):
        if (li[i][0] > li[j][1]) or (li[i][1] < li[j][0]):
            continue
        else:
            ans += 1
print(ans)