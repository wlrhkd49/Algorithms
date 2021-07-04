from collections import deque
n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split()))) 
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x,y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호 바이러스 먼저 증식)
data.sort()
q = deque(data)


s, x, y = map(int, input().split())

# 바이러스 증식 위치 4가지
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS 진행
while q:
    virus, t, X, Y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if t == s: # s초가 지난 경우
        break

    # 현재 위치에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<n:
            # 아직 방문하지 않은 위치라면 바이러스 전염
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, t+1, nx, ny))

print(graph[x-1][y-1])



