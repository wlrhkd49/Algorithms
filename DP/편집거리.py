# 1. 행과 열에 해당하는 문자가 서로 같다면, 
# 왼쪽 위에 해당하는 수를 그대로 대입
# 2. 행과 열에 해당하는 문자가 서로 다르다면, 
# 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당하는 수 중에서
# 가장 작은 수에 1을 더해 대입

# 최소 편집 거리 계산을 위한 DP
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # DP를 위한 2차원 DP 테이블 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]

    # DP 테이블 초기 설정
    for i in range(1, n+1): # (i,0) 초기 설정
        dp[i][0] = i
    for j in range(1, m+1): # (0,j) 초기 설정
        dp[0][j] = j
    
    # 최소 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위)
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
            
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1,str2))

