import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
# 중복값 제거 후 정렬
sorted_set_data = sorted(list(set(data)))

# 시간 단축을 위해 딕셔너리 인덱스 사용
dic = {sorted_set_data[i] : i for i in range(len(sorted_set_data))}

for d in data:
    print(dic[d], end=' ')