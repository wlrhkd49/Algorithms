while(True):
    x = input()
    result = 1
    if int(x) == 0:
        exit()
    else:
        for i in x:
            if i == '1':
                result+=3
            elif i == '0':
                result+=5
            else:
                result+=4
        print(result)
