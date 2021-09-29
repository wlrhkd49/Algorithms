data = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    data.append((x, y))

for d1 in data:
    rank = 1
    for d2 in data:
        if d1[0] < d2[0] and d1[1] < d2[1]:
            rank+=1
    print(rank, end = " ") 