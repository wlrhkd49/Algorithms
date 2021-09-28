n = int(input())
dp = [0] * (n+2)
dp[0], dp[1] = 0, 1

if n <= 1 :
    print(n)
else :
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])
