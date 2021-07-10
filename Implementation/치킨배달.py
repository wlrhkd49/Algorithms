# 조합을 사용하기 위한 라이브러리
from itertools import combinations

n, m = map(int, input().split())

house, chicken = [], []


for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c)) #일반 집
        elif data[c] == 2:
            chicken.append((r,c)) #치킨 집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken,m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(cx-hx)+abs(cy-hy))
        #가장 가까운 치킨집까지의 거리 더하기
        result += temp
    #치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
        

