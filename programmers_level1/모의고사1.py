def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_x = 0
    answer_y = 0
    answer_z = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            answer_x += 1
        if answers[i] == b[i%len(b)]:
            answer_y += 1
        if answers[i] == c[i%len(c)]:
            answer_z += 1
    
    if max(answer_x, answer_y, answer_z) == answer_x:
        answer.append(1)
    if max(answer_x, answer_y, answer_z) == answer_y:
        answer.append(2)
    if max(answer_x, answer_y, answer_z) == answer_z:
        answer.append(3)
        
    return answer