a, b = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
count = 0
for i in range(1,len(arr)):
    result += i

arr.sort()
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        count+=1

print(result-count)
