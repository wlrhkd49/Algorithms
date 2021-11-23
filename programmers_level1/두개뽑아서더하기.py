from itertools import combinations
def solution(numbers):
    answer = []
    arr = list(combinations(numbers, 2))
    for i in arr:
        x, y = i[0], i[1]
        if answer.count(x+y) == 0:
            answer.append(x+y)
    answer.sort()
    return answer
