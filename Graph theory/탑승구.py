# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 탑승구의 개수 입력
g = int(input())
# 비행기의 개수 입력
p = int(input())
# 부모 테이블 초기화
parent = [0] * (g+1)
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g+1):
    parent[i] = i

for i in range(p):
    # 현재 비행기 탑스구의 루트 확인
    data = find_parent(parent, int(input()))
    if data == 0: # 현재 루트가 0이라면, 종료 (비행기 못댐)
        break
    # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    union_parent(parent, data, data-1)
    result += 1

print(result)

# 입력 예시
# 4
# 3
# 4
# 1
# 1

# 출력 예시
# 2