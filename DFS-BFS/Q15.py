from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(m+1)]

# a노드에서 갈 수 있는 b노드를 graph에 삽입
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# distance 초기화
distance = [-1] * (n+1)
distance[x] = 0

# BFS수행
q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        # 처음 방문한 노드라면
        if distance[i] == -1:
            # 이전 노드 거리 + 1로 노드의 거리 초기화
            distance[i] = distance[now] + 1
            # 큐에 삽입
            q.append(i)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check=True

if check==False:
    print(-1)


