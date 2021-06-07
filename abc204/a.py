x, y = map(int, input().split())

if x==y:
    print(x)
elif (0 in (x,y)) and (1 in (x,y)):
    print(2)
elif (1 in (x,y)) and (2 in (x,y)):
    print(0)
else:
    print(1)