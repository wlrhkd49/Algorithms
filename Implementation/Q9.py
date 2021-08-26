def solution(s):
    answer = len(s)
    # 단위 1개 부터 늘려가면서 체크
    for step in range(1, len(s)//2 + 1):
        compressed = ''
        prev = s[0:step] # 맨 앞부터 step 크기만큼 문자열 추출
        count = 1
        for j in range(step, len(s), step):
            # 이전 상태와 동일한 문자열 나오면 count 증가
            if s[j: j+step] == prev:
                count+=1
            # 동일한 문자열이 안나온 경우
            else:
                compressed += str(count) + prev if count>=2 else prev
                prev = s[j: j+step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        # 만들어지는 압축 문자열이 가장 짧은 것 찾기
        answer = min(answer, len(compressed))
    return answer