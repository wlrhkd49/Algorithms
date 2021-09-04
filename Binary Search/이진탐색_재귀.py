# 이진 탐색 재귀
def binary_search(array, target, start, end):
    if start > end:
        None
    mid = (start+end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확ㅇ니
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# 원소의개수와 타겟을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소 존재 x")
else:
    print(result+1)