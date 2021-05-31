import math

A, B, W = map(int, input().split())
W *= 1000

max_num = int(math.floor(W/A))
min_num = int(math.ceil(W/B))

if min_num > max_num:
    print('UNSATISFIABLE')
else:
    print(min_num, max_num)