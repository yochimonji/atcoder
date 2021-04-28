n = str(input())
digit = len(n)

for _ in range(digit):
    if n == n[::-1]:
        print('Yes')
        exit()
    n = '0' + n
print('No')