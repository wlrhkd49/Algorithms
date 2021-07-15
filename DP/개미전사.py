# 정수 N 입력
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과 저장을 위한 DP 테이블 초기화
d = [0] * 100

# DP 진행 (bottom-up)
# ai = max(ai-1, ai-2 + ki) 
# 𝒂ᵢ = 𝑖번째 식량창고까지의 최적의 해 (얻을 수 있는 식량의 최댓값)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d)
print(d[n-1])