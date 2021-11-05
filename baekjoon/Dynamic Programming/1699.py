n = int(input())
dp = [0] * (n+1)
for i in range(1,n+1):
    dp[i] = i
    for j in range(1, i):
        # 제곱수가 i보다 커지면 멈춤
        if j*j > i:
            break
        # 제곱수로 표현할 때 가장 항의 개수가 작은 j를 찾음
        # 예를 들어 dp[6] = dp[6 - 2*2] + 1 은 2*2를 더한 경우 1가지를 추가하기 때문.
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
print(dp[n])