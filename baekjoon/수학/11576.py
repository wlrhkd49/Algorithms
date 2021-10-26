arr = []
for i in range(30):
    arr.append(i)

A, B = map(int, input().split())
m = int(input())
data = list(map(int,input().split()))
result = 0
data.reverse()
s = []
for i in range(len(data)):
    index = arr.index(data[i])
    result += index * pow(A, i)

while result:
    s.append(str(result%B))
    result //= B

s.reverse()
print(' '.join(s))
