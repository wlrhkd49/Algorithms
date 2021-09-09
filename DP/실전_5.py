# ai = min (ai, a(i-k)+1)
n, m = map(int, input().split())

# N개의 화폐 단위를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 dp테이블 초기화
d = [10001] * (m+1)

# dp 진행
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])