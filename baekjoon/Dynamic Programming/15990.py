MOD = 1000000009
dp = [[0] * (3) for _ in range(100001)]
dp[1] = [1, 0, 0] # 1로 끝나는 경우
dp[2] = [0, 1, 0] # 2로 끝나는 경우
# 2+1 : 1로 끝나는 경우
# 1+2 : 2로 끝나는 경우
# 3 : 3로 끝나는 경우
dp[3] = [1, 1, 1] 
for i in range(4, 100001):
    # 2, 3으로 끝난 숫자에 1 더하기
    dp[i][0] = (dp[i-1][1])%MOD + (dp[i-1][2]) % MOD 
    # 1, 3으로 끝난 숫자에 2 더하기
    dp[i][1] = (dp[i-2][0])%MOD + (dp[i-2][2]) % MOD
    # 1, 2으로 끝난 숫자에 3 더하기
    dp[i][2] = (dp[i-3][0])%MOD + (dp[i-3][1]) % MOD

for _ in range(int(input())):
    x = int(input())
    print(sum(dp[x])%MOD)