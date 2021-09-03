from typing import final


def solution(N, stages):
    answer = []
    n = len(stages)
    
    # 스테이지 번호를 1부터 증가 시키며
    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        # 실패율 계산
        if count == 0:
            fail = 0
        else:
            fail = count / n
            n-=count
        answer.append((i,fail))
    answer = sorted(answer, key = lambda x : (-x[1], x[0]))
    answer = [i[0] for i in answer]
    return answer