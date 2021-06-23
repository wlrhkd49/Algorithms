a, b = map(int, input().split())
result = 0 

# a가 b보다 크거나 같으면
while a>=b:
    # a가 b로 나누어떨어지지 않으면 -1
    while a%b != 0:
        a-=1
        result+=1
    # 나눠떨어지면 b로 나누기
    a//=b
    result+=1

# 남은 수에 대해서 -1 반복
while a>1:
    a-=1
    result+=1

print(result)
