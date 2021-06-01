def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in set(a):
        for j in set(c):
            if i == b[j-1]:
                ans += a.count(i) * c.count(j)
    print(ans)
solve()