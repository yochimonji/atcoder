def solve():
    from itertools import product

    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')

    for _bit in product((True, False), repeat=n-1):
        bit = list(_bit) + [True]
        score = 0
        cur = 0
        for i in range(n):
            cur |= a[i]
            if bit[i]:
                score ^= cur
                cur = 0
        ans = min(ans, score)
    print(ans)
solve()