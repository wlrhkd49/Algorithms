data = []
for _ in range(9):
    data.append(int(input()))

max_value = max(data)
index = data.index(max_value)

print(max_value)
print(index+1)
