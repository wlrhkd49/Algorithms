n = int(input())
count = 0
result = n
while 1:
    if len(str(result))==1:
        first = str(result)
    else:
        first = str(result)[1]
    if len(str(result))==1:
        second = str(result)
    else:
        second = int(str(result)[0]) + int(str(result)[1])
        if len(str(second)) == 1:
            second = str(second)
        else:
            second = str(second)[1]
    result = int(first + second)
    count += 1
    if result == n:
        break
    
print(count)
    