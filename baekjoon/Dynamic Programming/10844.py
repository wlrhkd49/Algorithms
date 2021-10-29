n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1): # i는 자리수
    for j in range(10):
        if j == 0: # 맨 뒤에 갈 수 있는 경우의 수가 0 일 경우
            # 왼쪽 대각선 위
            dp[i][j] = dp[i-1][1]
        elif j == 9: # 맨 뒤에 갈 수 있는 경우의 수가 9 일 경우
            # 왼쪽 대각선 위
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)