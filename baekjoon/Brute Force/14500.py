n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_num = max(map(max, graph))
max_value = 0
visited = [[0]*m for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, result):
    global max_value
    if result + max_num * (4-cnt) <= max_value:
        return
    if cnt == 4:
        if max_value < result:
            max_value = result
        return
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if cnt == 2:
                    visited[nx][ny] = 1
                    dfs(x, y, cnt+1, result + graph[nx][ny])
                    visited[nx][ny] = 0

                visited[nx][ny] = 1
                dfs(nx, ny, cnt+1, result + graph[nx][ny])
                visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0

print(max_value)