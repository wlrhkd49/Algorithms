from collections import deque
v, e, start = map(int, input().split())

graph = [[] for _ in range(v+1)]

visited = [False] * (v+1)

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        pop = queue.popleft()
        print(pop, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, start, visited)
print()
visited = [False] * (v+1)
bfs(graph, start, visited)

