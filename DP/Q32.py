n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        # 왼쪽 위에서 오는 경우
        if j == 0 :
            left_up = 0
        else :
            left_up = array[i-1][j-1]

        # 위에서 오는 경우
        if j == i:
            up = 0
        else:
            up = array[i-1][j]

        array[i][j] = array[i][j] + max(left_up, up)

print(max(array[n-1]))