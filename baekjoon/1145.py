data = list(map(int, input().split()))
value = 1
while True:
    count = 0
    for d in data:
        if value % d == 0:
           count+=1 
    if count>=3:
        print(value)
        break
    else:
        value += 1
    
