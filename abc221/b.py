s = input()
t = input()

if s == t:
    print('Yes')
    exit()

for i in range(len(s)-1):
    tmp_s = s[:i] + s[i+1] + s[i] + s[i+2:]
    if tmp_s == t:
        print('Yes')
        exit()

print('No')