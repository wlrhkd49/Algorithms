def bracket(data):
    count = 0
    for i in data:
        if i == '(':
            count += 1
        else:
            # 먼저 (가 나오지 않았는데 )이 나오는 경우
            # 올바른 괄호가 아님
            if count == 0:
                return False
            count -= 1
    if count == 0:
        return True
    else:
        return False

for _ in range(int(input())):
    data = input()
    ok = bracket(data)
    if ok == True:
        print('YES')
    else:
        print('NO')