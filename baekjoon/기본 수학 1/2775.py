for _ in range(int(input())):

    a = int(input())
    b = int(input())
    dp = [[0]*15 for _ in range(15)]
    for i in range(15):
        dp[0][i] = i

    for i in range(1, 15):
        for j in range(1, 15):
            result = 0 
            for k in range(1, j+1):
                result += dp[i-1][k] 
            dp[i][j] = result

    print(dp[a][b])
