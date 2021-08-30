n, m = map(int, input().split())

# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):

    # 주어진 범위를 벗어나면 종료
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상하좌우도 재귀적으로 호출
        # 연결된 모든 지점 방문
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        # graph[i][j] == 0 이라면 방문 시작
        if dfs(i,j) == True:
            result+=1

print(result)