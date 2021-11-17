def solution(n, words):
    answer = []
    flag = True
    cnt = 0
    
    for i in range(1, len(words)):
        # 앞 단어 맨 끝과 시작이 맞지 않는 경우
        if words[i-1][len(words[i-1])-1] != words[i][0]:
            flag = False
            answer.append((i % n) + 1)
            answer.append((i // n)+1)
            print(words[i], i)
            break
        if words[i] in words[:i]:
            flag = False
            print(words[i], i)
            answer.append((i % n) + 1)
            answer.append((i // n)+1)
            break
    if flag == True:
        answer.append(0)
        answer.append(0)
        

    return answer