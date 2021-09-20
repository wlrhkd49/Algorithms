for _ in range(int(input())):
    avg = 0
    count = 0
    data = list(map(int, input().split()))
    # 평균
    # 전체 합을 data의 개수로 나눈다
    avg = sum(data[1:])/data[0]
    for i in data[1:]:
        if i > avg:
            count += 1
    # 비율 계산 후 소수점 셋째 자리까지 표시
    x = round((count/data[0])*100, 3)
    print('%0.3f' % x+'%')
