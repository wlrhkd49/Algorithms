def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a==b:
                graph[a][b] = 0
                
    for e in road:
        a, b, c = e[0], e[1], e[2]
        if c < graph[a][b]:
            graph[a][b] = c
            graph[b][a] = c
    
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
                
    for a in range(1, N+1):
        if graph[1][a] <= K:
            answer += 1

    return answer