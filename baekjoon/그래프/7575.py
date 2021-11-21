from collections import deque
m, n = map(int, input().split())
queue = deque()
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny]==0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()
cnt = 0
for i in graph:
    for j in i:
        if j == 0:
            # 익지 않은 토마도 존재하면 -1 출력
            print(-1)
            exit(0)
    # 모두 익기 위해서 가장 높은 값 찾기
    cnt = max(cnt, max(i)) 
# 1부터 시작했으므로 1 빼줌
print(cnt-1)
