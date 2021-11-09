n, m, k = map(int,input().split())
data = [0] * (n+m+k+1)
for x in range(1, n+1):
    for y in range(1, m+1):
        for z in range(1, k+1):
            data[x+y+z] += 1

print(data.index(max(data)))
