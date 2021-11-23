from collections import deque
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(x, y, target_x, target_y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 1
    while queue:
        a, b = queue.popleft()
        if a == target_x and b == target_y:
            print(graph[a][b]-1)
            return
        for i in range(8):
            nx = a+dx[i]
            ny = b+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny] = graph[a][b]+1
                queue.append([nx, ny])                

for _ in range(int(input())):
    n = int(input())
    x, y = map(int,input().split())
    target_x, target_y = map(int, input().split())

    graph = [[0]*n for _ in range(n)]

    bfs(x, y, target_x, target_y)