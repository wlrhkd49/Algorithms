from itertools import combinations
data = []
for i in range(9):
    data.append(int(input()))

a = list(combinations(data, 2))
for d in a:
    if sum(data) - sum(d) == 100:
        data.remove(d[0])
        data.remove(d[1])

data.sort()

for x in data:
    print(x)