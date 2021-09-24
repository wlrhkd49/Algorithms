n = int(input())
result = 0

while n >= 0:
    # 5로 나누어 떨어지면 봉투 개수 출력
    if n%5 == 0:
        result += (n//5)
        print(result)
        break
    # 나누어떨어지지 않으면 전체 값에서 3을 빼고
    # 봉투개수를 하나 늘려줌
    n -= 3
    result+=1
# 마지막까지 5로 나눠지지 않은 경우 -1 출력
if n < 0:
    print(-1)