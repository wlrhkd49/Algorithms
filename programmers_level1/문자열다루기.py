def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s:
        if i.islower() or i.isupper():
            answer = False
            break
    return answer
