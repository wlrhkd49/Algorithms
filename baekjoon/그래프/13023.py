import sys
# 최대 재귀 횟수 제한을 풀어줌
sys.setrecursionlimit(10000)

v, e = map(int, input().split())
graph = [[] for i in range(v)]
visited = [False] * v

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cnt, v):
    if cnt == 4:
        print(1)
        sys.exit(0)

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, i)
            visited[i] = False

for i in range(v):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

print(0)
