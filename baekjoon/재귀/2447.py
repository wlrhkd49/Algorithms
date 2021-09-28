# 재귀 함수
def star_recursion(n):
    global data

    # 3x3 별찍기
    if n == 3:
        data[0][:3] = data[2][:3] = [1]*3
        data[1][:3] = [1, 0, 1]
        return

    # 3^i x 3^i 별 찍기
    a = n//3
    star_recursion(n//3)
    for i in range(3):
        for j in range(3):
            # 가운데 비워두기
            if i == 1 and j == 1:
                continue
            for k in range(a):
                data[a*i + k][a*j : a*(j+1)] = data[k][:a]

n = int(input())

data = [[0 for i in range(n)] for i in range(n)]

star_recursion(n)

for i in data :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()