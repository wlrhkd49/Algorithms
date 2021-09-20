i1 = int(input())
i2 = int(input())
i3 = int(input())
result = str(i1*i2*i3)
data = []
for i in range(len(result)):
    data.append(result[i])
for i in range(10):
    print(data.count(str(i)))