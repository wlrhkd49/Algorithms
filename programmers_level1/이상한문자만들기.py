def solution(s):
    answer = s.split(' ')
    
    for i in range(len(answer)):
        s = list(answer[i])
        for j in range(len(s)):
            if j % 2 == 0:
                s[j] = s[j].upper()
            else:
                s[j] = s[j].lower()
        answer[i] = ''.join(s)
    return ' '.join(answer)
