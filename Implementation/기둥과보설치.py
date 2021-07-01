def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: # 설치된 것이 기둥인 경우
            # 바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥 위라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False # 아니라면 거짓 반환
        elif stuff == 1: # 설치된 것이 보인 경우
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False # 아니라면 거짓 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1000개
        x,y,stuff,operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x,y,stuff]) # 일단 삭제 해본 뒤
            if not possible(answer): # 가능한 구조물 인지 확인
                answer.append([x,y,stuff]) # 가능한 구조물이 아니라면 다시 설치
                
        if operate == 1: # 설치하는 경우
            answer.append([x,y,stuff]) # 일단 설치 해본 뒤
            if not possible(answer): # 가능한 구조물 인지 확인
                answer.remove([x,y,stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer)
            