w, h = map(int, input().split())

result = 0

for i in range(w):
    # 행마다 데이터 입력받기
    data = list(map(int, input().split()))
    # 최소값 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # 각 행의 최소값 중 최대값 찾기
    result = max(min_value, result)

print(result)