import math

n = int(input())
ans = float('inf')
for i in range(math.floor(math.sqrt(n))):
    if n % (i+1) == 0:
        ans = min(max(len(str(i+1)), len(str(n//(i+1)))), ans)
print(ans)