n = int(input())
data = list(map(int, input().split()))
result = 0
max_value = max(data)

for i in range(len(data)):
    data[i] = data[i]/max_value*100
    result += data[i]

print(sum(data)/len(data))
