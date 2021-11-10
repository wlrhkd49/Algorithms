for tc in range(int(input())):
    n = int(input())
    data = []
    for i in range(2):
        data.append(list(map(int, input().split())))
    for i in range(1, n):
        if i == 1:
            data[0][i] += data[1][i-1]
            data[1][i] += data[0][i-1]
        else:
            data[0][i] += max(data[1][i-1], data[1][i-2])
            data[1][i] += max(data[0][i-1], data[0][i-2])
    print(max(data[0][n-1], data[1][n-1]))

