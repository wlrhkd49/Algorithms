# 플로이드 워셜 알고리즘
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 K와 최종 목적지 노드 X를 입력
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
dist = graph[1][k] + graph[k][x]

# 도달할 수 없으면 -1 출력
if dist >= INF:
    print("-1")
# 도달할 수 있으면 결과 출력
else:
    print(dist)