n = int(input())
prev_x = 0
prev_y = 0
prev_t = 0

for i in range(n):
    t, x, y = map(int, input().split())
    length = abs(x-prev_x) + abs(y-prev_y)
    time = t - prev_t
    if (time < length) or (time + length) % 2:
        print('No')
        exit()
    prev_x = x
    prev_y = y
    prev_t = t
print('Yes')