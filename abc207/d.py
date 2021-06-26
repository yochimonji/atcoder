import copy, math

n = int(input())
s = []
t = []
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(n):
    t.append(list(map(int, input().split())))

def is_same(s, t):
    for ss in s:
        if ss not in t:
            print(ss)
            return False
    return True

degree = math.atan2(t[0][1], t[0][0]) - math.atan2(t[1][1], t[1][0])
for i in range(len(s)-1):
    s_copy = copy.deepcopy(s)
    t_copy = copy.deepcopy(t)
    dx = s_copy[i][0] - t_copy[i][0]
    dy = s_copy[i][1] - t_copy[i][1]
    