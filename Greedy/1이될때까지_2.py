a, b = map(int, input().split())
result = 0 

while True:
    # (a == b로 나눠지는 수 될 때까지 1씩 빼기)
    target = (a//b) * b
    result += (a-target)
    a = target

    # a이 b보다 작을 때 더이상 나눌 수 없으므로 반복문 탈출
    if a<b:
        break

    result += 1
    a//=b

result += (a-1)
print(result)