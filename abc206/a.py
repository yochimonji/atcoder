import math

n = int(input())

x = math.floor(n * 1.08)
if x < 206:
    print('Yay!')
elif x == 206:
    print('so-so')
else:
    print(':(')