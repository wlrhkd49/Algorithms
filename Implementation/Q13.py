from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i,j))
        elif data[j] == 2:
            chicken.append((i,j))

# 모든 치킨집 중에서 m개의 치킨집 뽑음
candidates = list(combinations(chicken, m))

# 치킨 거리 합 계산
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)