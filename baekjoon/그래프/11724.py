import sys
# 최대 재귀 횟수 제한을 풀어줌
sys.setrecursionlimit(10000)
v, e = map(int, input().split())
graph = [[] for i in range(v+1)]
visited = [False] * (v+1)

for i in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

def DFS(graph, start, visited):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

count = 0 

for i in range(1, v+1):
    if visited[i] == False:
        count += 1
        DFS(graph, i, visited)

print(count)