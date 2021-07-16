n = int(input())

# 앞 서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# DP 진행 (bottom-up)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = ( d[i-1] + 2 * d[i-2] ) % 796796

# 계산된 결과 출력
print(d[n])