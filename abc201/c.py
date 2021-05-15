import math

S = input()

# exist_num = 0
# no_know_num = 0

# for s in S:
#     if s=='o':
#         exist_num += 1
#     elif s=='?':
#         no_know_num += 1
# if exist_num >= 5 or (exist_num == 0 and no_know_num == 0):
#     print(0)


# print()

from itertools import product

exist_list = []
no_know_list = []
for i,s in enumerate(S):
    if s == 'o':
        exist_list.append(i)
    elif s == '?':
        no_know_list.append(i)

if len(exist_list) >= 5 or (len(exist_list) == 0 and len(no_know_list) == 0):
    print(0)
    exit()

ans = len(list(product(exist_list+no_know_list, repeat=4)))
for i in product(exist_list+no_know_list, repeat=4):
    for j in exist_list:
        if j not in i:
            ans -= 1
            break
print(ans)