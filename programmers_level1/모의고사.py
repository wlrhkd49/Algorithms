def solution(answers):
    answer = []
    arr = []
    length = len(answers)
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    result_a = 0
    result_b = 0
    result_c = 0
    
    for i in range(length):
        if answers[i] == a[i%5]:
            result_a += 1
        if answers[i] == b[i%8]:
            result_b += 1
        if answers[i] == c[i%10]:
            result_c += 1
    
    arr.append(result_a)
    arr.append(result_b)
    arr.append(result_c)
    
    for i, value in enumerate(arr):
        if value == max(arr):
            answer.append(i+1)
    
    return answer