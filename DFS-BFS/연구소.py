n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽 설치 후 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 방향 이동 리스트 동, 서, 남, 북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용하여 각 바이러스가 사방으로 퍼지게 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 바이러스가 퍼질 수 있는 위치라면
        if nx>=0 and nx<n and ny>=0 and ny<m :
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고 dfs 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx,ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메소드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: # 안전 영역이라면
                score += 1

    return score

# dfs로 울타리 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        # 각 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2: # 바이러스 있는 위치라면 dfs 바이러스 진행
                    virus(i,j)

        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    
    # 빈 공간에 울타리 설치
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