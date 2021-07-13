def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개 이므로 0 반환
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수 반환
    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # 가장 왼쪽에 있는 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid 
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)
    
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # 가장 오른쪽에 있는 인덱스 반환
    if (mid == len(array)-1 or target < array[mid+1]) and array[mid] == target:
        return mid 
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

N, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 x인 데이터의 개수 계산:
count = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
else:
    print(count)