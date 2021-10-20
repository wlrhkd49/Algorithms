for i in input():
    if i.isalpha():
        print(chr(ord(i)+13),end='')
    else:
        print(end=' ')
