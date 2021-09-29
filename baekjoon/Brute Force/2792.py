from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
combs = list(combinations(data, 3))

for comb in combs:
    if sum(comb)<=m:
        result = max(result, sum(comb))

print(result)

