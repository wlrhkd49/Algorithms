from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] != 0:
            queue.append(((100-progresses[i]) // speeds[i]) + 1)
        else:
            queue.append(((100-progresses[i]) // speeds[i]))
    x = queue.popleft()
    cnt=1
    while queue:
        y = queue.popleft()
        if x < y:
            answer.append(cnt)
            cnt = 1
            x = y
        else:
            cnt += 1
        if not queue:
            answer.append(cnt)
    return answer