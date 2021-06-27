n = int(input())
a = list(map(int, input().split()))
a.sort()
if len(a)==1:
    if a[0]==1:
        print('Yes')
    else:
        print('No')
    exit()
    
for i in range(len(a)-1):
    if a[i+1]-a[i]!=1:
        print('No')
        exit()
print('Yes')