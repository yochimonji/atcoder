h, w = map(int, input().split())

a = []

for i in range(h):
    a.append(list(map(int, input().split())))

for i2 in range(1, h):
    for j2 in range(1, w):
        for i1 in range(i2):
            for j1 in range(j2):
                if a[i1][j1] + a[i2][j2] > a[i2][j1] + a[i1][j2]:
                    print('No')
                    exit()
print('Yes')