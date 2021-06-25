n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())

d[x][y]=1 # 현재 좌표 방문
array = [] # 맵 모양을 알려줄 array
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 돌기
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 앞으로 전진할 수 있으면 전진!
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 방문 표시
        x,y = nx, ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    
    # 네 방향 전부 가지 못하는 경우
    if turn_time==4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        turn_time=0
        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 바다로 막힌 경우
        else:
            break

print(count)

