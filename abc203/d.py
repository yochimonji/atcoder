import math, statistics

N, K = map(int, input().split())
A = [list(map(int, input().split())) for j in range(N)]

med = float('inf')
for i in range(N-K+1):
    temp_med = []
    for j in range(N-K+1):
        for ki in range(K):
            for kj in range(K):
                temp_med.append(A[i+ki][j+kj])
        med = min(med, statistics.median_low(temp_med))
        print(temp_med, statistics.median_low(temp_med))
print(med)