from collections import deque

t = deque()
flip = False

for s in input():
    if s=='R':
        flip = not flip
    elif flip:
        if t and (t[0] == s):
            t.popleft()
        else:
            t.appendleft(s)
    else:
        if t and (t[-1] == s):
            t.pop()
        else:
            t.append(s)
if flip:
    t = reversed(t)
print(''.join(t))