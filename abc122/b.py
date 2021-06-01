s = input()

ans = 0
temp = ''
for i in s:
    if i in 'ACGT':
        temp = temp + i
    else:
        ans = max(ans, len(temp))
        temp = ''
ans = max(ans, len(temp))
print(ans)