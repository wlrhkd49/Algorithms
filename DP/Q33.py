n = int(input())
dp = [0] * (n+1)
t = []
p = []
max_value = 0 # 최대 이익

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1): # 거꾸로 계산
    time = i + t[i]

    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        # 현재값 + 마지막 날까지 낼 수 있는 최대 이익
        max_value = dp[i]

    else:
        dp[i] = max_value

print(max_value)


