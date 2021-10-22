# 유클리드 호제법 최대공약수
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
# 유클리드 호제법 이용한 최소공배수
def lcm(a,b):
    return (a*b)//gcd(a,b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a,b))