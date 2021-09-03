n = int(input())

data = []
for i in range(n):
    data.append(list(input().split()))

data = sorted(data, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

print(data)