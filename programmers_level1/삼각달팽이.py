def solution(n):
    answer = []
    x, y = -1, 0
    num = 1
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            
            # down 방향으로 진행
            if i % 3 == 0:
                x += 1
            # right 방향으로 진행
            elif i % 3 == 1:
                y += 1
            # up 방향으로 진행
            else:
                x -= 1
                y -= 1
            tmp[x][y] = num
            num += 1
    
    for i in tmp:
        for j in i:
            if j != 0:
                answer.append(j)
    
    return answer