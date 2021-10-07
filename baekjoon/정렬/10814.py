import sys
input = sys.stdin.readline

data = []
for i in range(int(input())):
    x, y = input().split()
    data.append((x, y, i))

data.sort(key = lambda x: (int(x[0]), x[2]))

for d in data:
    print(d[0], d[1])
