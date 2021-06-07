n, m = map(int, input().split())
graph = {}
for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] not in graph.keys():
        graph[temp[0]] = []
    graph[temp[0]].append(temp[1])

def solve(key, went_location):
    new_location = set()
    temp_ans = 0
    for loc in graph[key]:
        if loc not in went_location:
            new_location.add(loc)
            temp_ans += 1
    for loc in new_location:
        temp_ans += solve(loc, went_location)
    return temp_ans

ans = 0
for key in graph.keys():
    went_location = set([key])
    ans += solve(key, went_location)
print(ans)