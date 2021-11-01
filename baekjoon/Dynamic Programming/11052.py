n = int(input())
data = list(map(int, input().split()))

dp = [0] * (n+1)
dp[0] = 0
dp[1] = data[0]

# dp[2] = dp[1] + data[0] or dp[0] + data[1]
# dp[3] = dp[2] + data[0] or dp[1] + data[1] or d[0] + data[2]
# dp[4] = dp[3] + data[0] or dp[2] + data[1] or dp[1] + data[2] + dp[0] + dp[3]
for i in range(2, n+1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + data[j-1]:
            dp[i] = dp[i - j] + data[j-1]
print(dp[n])
