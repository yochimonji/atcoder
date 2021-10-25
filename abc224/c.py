from itertools import combinations

n = int(input())

dot = []
for i in range(n):
    dot.append(list(map(int, input().split())))

ans = 0
for i in combinations(dot, 3):
    if (abs(i[2][0]-i[0][0]) * abs(i[1][1]-i[0][1])) != (abs(i[1][0]-i[0][0]) * abs(i[2][1]-i[0][1])):
        ans += 1
print(ans)