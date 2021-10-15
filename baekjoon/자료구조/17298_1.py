import sys
input = sys.stdin.readline
data = [0] * 1000000
n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    data[arr[i]] = i

for i in range(len(arr)):
    x = arr[i]
    for j in range(x+1, len(data)):
        if data[j] != 0 and i < data[j]:
            print(j, end=' ')
            break
        if j == len(data)-1:
            print(-1, end=' ')