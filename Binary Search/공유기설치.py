# 집의 개수와 공유기의 개수 입력
n, c = list(map(int, input().split()))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = array[1] - array[0] # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값
result = 0

while(start<=end):
    mid = (start+end)//2 # mid는 가장 인접한 두 공유기 사이의 거리: gap
    value = array[0]
    count = 1

    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n): # 앞에서 부터 gap에 따라 설치 해보기
        if array[i] >= value + mid:
            value = array[i]
            count+=1

    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = count # 최적의 결과 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)