for _ in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))

    # DP를 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    # DP 진행
    for j in range(1,m):
        for i in range(n):
            # 위에서 오는 경우
            if i == 0: # 맨 위에 있으면 왼쪽 위가 없음
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: # 맨 아래에 있으면 왼쪽 아래가 없음
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽 에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1]) # 맨 끝열중 가장 큰 값
    print(result)