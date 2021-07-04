# https://programmers.co.kr/learn/courses/30/lessons/60058 에서 실행
# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# 올바른 괄호 문자열 인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count+=1
        else:
            if count == 0:
                return False # 쌍이 안맞으면 False
            count -= 1
    return True # 쌍이 맞는 경우에 True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    # 문자열 u가 "올바른 괄호 문자열" 이라면
    if check_proper(u) == True:
        answer = u + solution(v)
        
    # 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
                
        answer += "".join(u)
        
    return answer