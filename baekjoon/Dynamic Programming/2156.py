data = []
n = int(input())
for i in range(n):
    data.append(int(input()))
dp = [0] * n
dp[0] = data[0]
dp[1] = data[0]+data[1]
dp[2] = max(dp[1], data[1]+data[2], data[2]+data[0])

# 현재 위치 포도주 안마시기
# 전전 포도주 안마시고 현재 위치 포도주 마시기
# 전 포도주 안마시고 현재 위치 포도주 마시기
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+data[i-1]+data[i], dp[i-2]+data[i])
print(dp[n-1])