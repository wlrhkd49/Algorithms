import sys
input = sys.stdin.readline

# 에라토스테네스의 체
# 전체 수 만큼 True 리스트 생성
# 2부터 1씩 더해주면서 그 배수에 해당하는 값들을 False로 바꾼다.
array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

tc = int(input())
for i in range(tc):
    n = int(input())
    count = 0
    
    for i in range(2, n//2+1):
        if array[i] and array[n-i]:
            count+=1

    print(count)