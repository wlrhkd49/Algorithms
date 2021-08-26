n = input()
result = 0
array = []

for i in range(len(n)):
    if(n[i].isdigit()):
        result+=int(n[i])
    else:
        array.append(n[i])

array.sort()

if(result != 0):
    array.append(result)

for a in array:
    print(a,end='')

print(''.join(array))
