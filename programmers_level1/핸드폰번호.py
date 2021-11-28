def solution(phone_number):
    answer = []
    for i in phone_number:
        answer.append(i)
    answer1 = answer[:-4]
    answer2 = answer[-4:]
    for i in range(len(answer1)):
        answer1[i] = '*' 
        
    return ''.join(answer1 + answer2)
