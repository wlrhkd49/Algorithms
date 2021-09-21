n = int(input())
count = 99

if n<=99:
    print(n)
else:
    for i in range(100, n+1):
        s = str(i)
        if int(s[2])-int(s[1]) == int(s[1])-int(s[0]):
            count+=1
    print(count) 
