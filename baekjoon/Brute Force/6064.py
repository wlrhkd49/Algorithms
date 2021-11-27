def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

def lcm(x,y):
    return (x*y)//gcd(x,y)
    

def solution(M, N, target_x, target_y):
    while target_x <= lcm(M, N):
        if (target_x - target_y) % N == 0:
            return target_x
        target_x += M
    return -1

for _ in range(int(input())):
    M, N, target_x, target_y = map(int, input().split())
    print(solution(M, N, target_x, target_y))

            
