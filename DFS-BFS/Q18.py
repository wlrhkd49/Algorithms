# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# 올바른 괄호 문자열 인지 판단
def check_proper(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            if count == 0: # 쌍 안맞으면 False
                return False 
            count -= 1
    return True # 쌍 맞으면 True
    

def solution(p):
    answer = ''
    if p == '':
        return answer
    
    # 균형잡힌 인덱스 번호 찾기
    index = balanced_index(p)
    u = p[:index+1] # 설명 2 부분
    v = p[index+1:] # 설명 2 부분
    
    if check_proper(u) == True:
        answer = u + solution(v)
    
    else:
        answer = '(' + solution(v) + ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
    
    return answer