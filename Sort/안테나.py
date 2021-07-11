n = int(input())
arr = list(map(int, input().split()))

print(arr)

result = 1e9
final = 1

for i in range(1,10):
    temp = 0
    for j in range(n):
        temp += abs(i-arr[j])
    if result>temp:
        final = i
    result = min(result, temp)
    
print(final)