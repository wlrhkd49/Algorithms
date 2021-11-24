# 유클리드 호제법
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
    
def lcm(a, b):
    return (a*b) // gcd(a, b)

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer