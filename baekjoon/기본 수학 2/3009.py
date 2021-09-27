dataX = []
dataY = []
for _ in range(3):
    x, y = map(int, input().split())
    if dataX.count(x) == 1:
        dataX.remove(x)
    else:
        dataX.append(x)
    if dataY.count(y) == 1:
        dataY.remove(y)
    else:
        dataY.append(y)
print(dataX[0], dataY[0])