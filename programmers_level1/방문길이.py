def solution(dirs):
    answer = []
    cnt = 0
    x = 0
    y = 0
    # U, D, R, L
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for dir in dirs:
        if dir == 'U':
            x += dx[0]
            y += dy[0]
            if x < -5 or x > 5 or y < -5 or y > 5:
                x -= dx[0]
                y -= dy[0]
                continue
            if ((x-dx[0], y-dy[0], x, y)) in answer:
                continue
            answer.append((x-dx[0], y-dy[0], x, y))
            answer.append((x, y, x-dx[0], y-dy[0]))
            cnt += 1
        if dir == 'D':
            x += dx[1]
            y += dy[1]
            if x < -5 or x > 5 or y < -5 or y > 5:
                x -= dx[1]
                y -= dy[1]
                continue
            if ((x-dx[1], y-dy[1], x, y)) in answer:
                continue
            answer.append((x-dx[1], y-dy[1], x, y))
            answer.append((x, y, x-dx[1], y-dy[1]))
            cnt += 1
        if dir == 'R':
            x += dx[2]
            y += dy[2]
            if x < -5 or x > 5 or y < -5 or y > 5:
                x -= dx[2]
                y -= dy[2]
                continue
            if ((x-dx[2], y-dy[2], x, y)) in answer:
                continue
            answer.append((x-dx[2], y-dy[2], x, y))
            answer.append((x, y, x-dx[2], y-dy[2]))
            cnt += 1
        if dir == 'L':
            x += dx[3]
            y += dy[3]
            if x < -5 or x > 5 or y < -5 or y > 5:
                x -= dx[3]
                y -= dy[3]
                continue
            if ((x-dx[3], y-dy[3], x, y)) in answer:
                continue
            answer.append((x-dx[3], y-dy[3], x, y))
            answer.append((x, y, x-dx[3], y-dy[3]))
            cnt += 1
            
    return cnt
