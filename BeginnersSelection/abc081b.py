n = int(input())
A = list(map(int, input().split()))

# 1つ目
# ans = 0
# while all(a%2==0 for a in A):
#     ans += 1
#     A = list(map(lambda i: i//2, A))

# 2つ目
ans = float('inf')
for a in A:
    ans = min(ans, len(bin(a)) - bin(a).rfind('1') -1)
print(ans)