for i in input():
    # 대문자: 65 ~ 90
    if i.isupper():
        if ord(i)+13 <=90:
            print(chr(ord(i)+13),end='')
        else:
            print(chr(ord(i)-13),end='')
    # 소문자 97 ~ 122
    elif i.islower():
        if ord(i)+13 <=122:
            print(chr(ord(i)+13),end='')
        else:
            print(chr(ord(i)-13),end='')
    else:
        print(i, end='')
