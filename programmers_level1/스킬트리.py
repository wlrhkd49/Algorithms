def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_have = []
        flag = True
        
        # 스킬트리 중 스킬을 한 문자씩 검사
        for s in skills:
            if s in skill:
                skill_have.append(s)
        for k in range(len(skill_have)):
            if skill[k] != skill_have[k]:
                flag = False
                break
        if flag == True:
            answer += 1
            
    return answer