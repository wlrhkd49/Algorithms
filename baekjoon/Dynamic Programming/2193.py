n = int(input())
dp = [[0] * 2 for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2,n+1):
    for j in range(2):
        if j == 1:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j]

print(sum(dp[n]))