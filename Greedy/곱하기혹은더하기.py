a = input()
result = int(a[0])

for i in range(1, len(a)):
    num = int(a[i]) # 배열값을 하나씩 저장 
    if num <= 1 or result <= 1: # 수가 0 or 1이면 덧셈 수행
        result+=num
    else: # 1보다 큰 수이면 곱셈 진행
        result*=num

print(result)