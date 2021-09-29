n =int(input())
result = 0

# n보다 작거나 같은 수 모두 확인
for i in range(1, n+1):
    #각 자리수를 담은 리스트
    data = list(map(int, str(i)))    
    # i와 각 자리수의 합
    result = i + sum(data)

    # 1부터 시작하므로 생성자 찾으면 출력하고 반복문을 벗어남
    if n == result:
        print(i)
        break

    # 못찾은 경우 0 출력
    if i == n:
        print(0)