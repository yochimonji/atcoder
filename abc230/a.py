n = input()

if len(n) == 2:
    if int(n) >= 42:
        print('AGC0{}'.format(int(n)+1))
    else:
        print('AGC0{}'.format(int(n)))
else:
    print('AGC00{}'.format(n))