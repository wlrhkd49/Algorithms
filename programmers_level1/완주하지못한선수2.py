# 해시를 이용한 풀이법
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for i in participant:
        hashDict[hash(i)] = i
        sumHash += hash(i)
    
    for j in completion:
        sumHash -= hash(j)
    
    return hashDict[sumHash]