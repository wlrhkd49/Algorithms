n = int(input())
arr = list(input().split())
x=1
y=1
for i in range(len(arr)):
    if(arr[i] == 'R'):
        if(y==n):
            continue
        y+=1
    elif(arr[i] == 'L'):
        if(y==1):
            continue
        y-=1
    elif(arr[i] == 'U'):
        if(x==1):
            continue
        x-=1
    else:
        if(x==n):
            continue
        x+=1

print(x, y)
