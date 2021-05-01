S = input()
t = str()
flip = False
for s in S:
    if s=='R':
        flip = not flip
    else:
        if flip:
            t = s+t
            if t[:2:] == s+s:
                t = t[2::]

        else:
            t = t+s
            if t[-2::] == s+s:
                t = t[:-2:]
if flip:
    t = t[::-1]
print(t)