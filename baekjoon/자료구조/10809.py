data = [-1] * 26
cnt = 0

for i in input():
    # index를 찾음
    x = ord(i)-ord('a')
    # 처음 입력된 값이면 위치(cnt)로 변경
    if data[x] == -1:
        data[x] = cnt
    # cnt를 1씩 증가
    cnt += 1
    
for d in data:
    print(d, end = ' ')
