n = int(input())

x = 0
for i in range(n):
    x += i+1
    if x >= n:
        print(i+1)
        exit()