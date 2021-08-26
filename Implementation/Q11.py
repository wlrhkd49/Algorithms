n = int(input())
k = int(input())

data = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 오른쪽 시작 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = ((direction)-1) % 4
    else:
        direction = ((direction)+1) % 4
    return direction

def simul():
    x, y = 1, 1
    data[x][y] = 2 # 뱀 존재 표시
    direction = 0 # 동, 남, 서, 북
    time = 0 # 시작한 뒤 지난 시간
    index = 0 # 다음 회전 정보
    q = [(x,y)] # 뱀이 차지한 위치
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]

        if nx >= 1 and ny >= 1 and nx <= n and ny <= n and data[nx][ny] != 2:
            # 사과 없으면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0

            # 사과 있다면 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        #벽이나 몸통에 부딪힌 경우
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]: #회전할 시간인 경우
            direction = turn(direction, info[index][1]) # 방향과 L or R
            index += 1
    return time

print(simul())

