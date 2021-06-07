import math, re

n = int(input())
s = input()

ans = 0
for i in range(1000):
    if len(str(i)) == 1:
        pattern = '00' + str(i)
    elif len(str(i)) == 2:
        pattern = '0' + str(i)
    else:
        pattern = str(i)
    
    for p in pattern:
        
print(ans)