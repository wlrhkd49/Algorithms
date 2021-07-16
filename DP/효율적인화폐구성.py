# 정수 n, m 입력
n, m = map(int, input().split())
array = []

# N개의 화폐 단위 정보 입력
for _ in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# DP 진행 (bottom-up)
d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        # i-k원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는경우
    print(-1)
else:
    print(d[m])
