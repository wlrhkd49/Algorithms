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

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

# union 연산을 수행
for i in range(v):
    data = list(map(int, input().split()))
    for j in range(v):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

# 여행 계획 입력
data = list(map(int, input().split()))
result = True

for i in range(e-1):
    if find_parent(parent, data[i]) != find_parent(parent, data[i+1]):
        result = False

if result == False:
    print("NO")
else:
    print("YES")

# 입력 예시
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

# 출력 예시
# YES