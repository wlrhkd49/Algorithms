from collections import deque

# 테스트 케이스만큼 반복
for tc in range(int(input())):
    # 노드의 개수 입력
    n = int(input())
    # 모든 노드의 진입 차수는 0으로 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n+1) for _ in range(n+1)]

    # 작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True # 자신보다 작은 노드로 방향
            indegree[data[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬 시작
    result = [] # 알고리즘 수행 결과 리스트
    q = deque() # 큐 기능 라이브러리

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상 정렬 결과가 오직 하나인지
    cycle = False # 그래프 내 사이클이 존재하는지

    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클 발생
        if len(q) == 0:
            cycle = True
            break

        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개
        if len(q) >= 2:
            certain = False
            break

        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in range(1, n+1):
            if graph[now][i]: # True라면
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    # 사이클이 발생하는 경우 ( 일관성 x )
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬의 결과가 여러 개인 경우
    elif not certain:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in result:
            print(i, end = ' ')
        print()


