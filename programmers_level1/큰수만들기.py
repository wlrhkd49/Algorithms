def solution(number, k):
    answer = [number[0]]
    for i in range(1, len(number)):
        if k > 0:
            while answer[-1] < number[i]:
                k-=1
                answer.pop()
                if not answer or k==0:
                    break
        answer.append(number[i])
    
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)