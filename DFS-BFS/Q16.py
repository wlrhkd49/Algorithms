n, m = map(int, input().split())
temp = [[0] * m for _ in range(n)]
data = []

for i in range(n):
    data.append(list(map(int, input().split())))


# 4가지 방향 이동 리스트 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

# DFS를 이용하여 각 바이러스가 사방으로 퍼지게 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메소드
def get_score():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    return count 

# dfs로 울타리 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 바이러스 퍼지게 하기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        result = max(result, get_score())
        return


    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

