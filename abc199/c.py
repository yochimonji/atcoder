n = int(input())
s = list(input())
q = int(input())
flag = False

for i in range(q):
    t, a, b = map(int, input().split())
    if t==1:
        if flag:
            if a <= n:
                a = a + n
            else:
                a = a - n
            if b <= n:
                b = b + n
            else:
                b = b - n
        temp = s[a-1]
        s[a-1] = s[b-1]
        s[b-1] = temp
    else:
        if flag:
            flag = False
        else:
            flag = True

if flag:
    temp = s[:n]
    s[:n] = s[n:]
    s[n:] = temp
print(''.join(s))