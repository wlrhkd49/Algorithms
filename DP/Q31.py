for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int,input().split()))

    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    # dp 진행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)