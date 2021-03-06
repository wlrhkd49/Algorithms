n = int(input())
dp = []

# DP 테이블 초기화
for i in range(n):
    dp.append(list(map(int,input().split())))

# DP로 두 번째 줄부터 내려가면서 확인
for i in range(1,n):
    for j in range(i+1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        # 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        # 최대 합 저장
        dp[i][j] = dp[i][j] + max(up_left, up)
#result = 0 
#for i in range(n):
#    result = max(result, dp[n-1][i])
print(max(dp[n-1]))
    
    