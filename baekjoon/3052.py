data = []
for _ in range(10):
    data.append(int(input())%42)

data = set(data)
print(len(data))