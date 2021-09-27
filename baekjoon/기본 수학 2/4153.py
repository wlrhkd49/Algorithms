while 1:
    data = list(map(int, input().split()))
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        break
    max_value = max(data)
    data.remove(max_value)

    if max_value**2 == data[0]**2 + data[1]**2:
        print('right')
    else:
        print('wrong')