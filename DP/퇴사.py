# d[i] = i 번째 날부터 마지막 날까지 낼 수 있는 최대 이익
# d[i] = max(p[i] + dp[t[i]+i]], max_value)
# max_value : 현재까지의 최대 상담 금액에 해당하는 변수

n = int(input())
t = [] # 각 상담을 완료하는데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n) # DP를 위한 1차원 DP 테이블
max_value = 0

for _ in range(n) :
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담 기간이 벗어나는 경우
    else:
        dp[i] = max_value

print(dp)
print(max_value)
