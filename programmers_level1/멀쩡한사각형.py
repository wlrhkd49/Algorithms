def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(w,h):
    answer = 1
    x = gcd(w,h)
    # answer = (w * h) - x * (w//x + h//x - 1)
    answer = (w * h) - (w + h - x)
    return answer