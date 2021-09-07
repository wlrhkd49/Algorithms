n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

# mid를 gap으로 설정하여 gap의 크기를 늘리거나 줄이면서 최적의 해를 찾음
while start<=end:
    mid = (start+end)//2
    value = array[0]
    count = 1
    for i in range(1, n):
        # gap 보다 거리가 길면 공유기 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과 저장
    else: # 설치를 못하는 경우, 거리를 감소
        end = mid - 1

print(result)

        

