from collections import deque

n, k = map(int, input().split())

data = []
virus = []

# 상, 하, 좌, 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            # 바이러스 종류, 시간, 위치 x, 위치 y
            virus.append((data[i][j], 0, i, j))

target_s, target_x, target_y = map(int, input().split())

# 정렬 이후에 큐로 옮기기
virus.sort()
q = deque(virus)

while q:
    v, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있으면 전염 후 큐에 삽입
        if nx>=0 and ny>=0 and nx<n and ny<n:
            if data[nx][ny] == 0:
                data[nx][ny] = v
                q.append((v, s+1, nx, ny))

print(data[target_x-1][target_y-1])




