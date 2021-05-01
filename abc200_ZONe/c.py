n = int(input())
member = []
score = 0

for _ in range(n):
    member.append(list(map(int, input().split())))

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            score = max(score, min([max(member[i][l], member[j][l], member[k][l]) for l in range(5)]))
print(score)