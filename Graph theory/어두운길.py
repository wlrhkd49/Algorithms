def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v)
edges = []

for i in range(v):
    parent[i] = i

for i in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost # 전체 비용 합
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost # 설치에 필요한 비용
        union_parent(parent, a, b)

print(total - result) # 절약할 수 있는 값

# 입력 예시
# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

# 출력 예시
# 51