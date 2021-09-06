n,m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in array:
        if x > mid:
            total += (x-mid)
    # 부족한 경우
    if total < m:
        end = mid - 1
    # 더 양이 많은 경우 (일단 기록)
    else:
        result = mid
        start = mid + 1
    
print(result)