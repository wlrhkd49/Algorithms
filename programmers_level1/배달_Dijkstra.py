import heapq
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    start = 1
    graph = [[] for i in range(N+1)]
    distance = [INF] * (N+1)
    
    for e in road:
        a, b, c = e[0], e[1], e[2]
        # a노드에서 b노드로 가는 비용 c
        graph[a].append((b,c))
        # b노드에서 a노드로 가는 비용 c
        graph[b].append((a,c))
        
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    for i in range(1, N+1):
        if distance[i] <= K:
            answer+=1
    
    return answer