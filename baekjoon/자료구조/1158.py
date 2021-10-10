n, k = map(int, input().split())
data = []
result = []
num = 0
for i in range(1, n+1):
    data.append(i)

for i in range(n):
    num = (num+k-1)%len(data)
    result.append(str(data.pop(num)))

print("<", ", ".join(result), ">", sep="")

