def solution(num):
    answer = 0
    while num != 1:
        answer += 1
        # 500번 이상 시 -1 출력
        if answer >= 500:
            answer = -1
            break
        # 짝수면 2로 나눔
        if num % 2 == 0:
            num = num // 2
            
        # 홀수면 3을 곱하고 1을 더함
        else:
            num = num * 3 + 1
    return answer
