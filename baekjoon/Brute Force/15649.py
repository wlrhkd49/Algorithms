n, m = map(int, input().split())
arr = [] 

def dfs():
    if len(arr) == m:
        # arr을 ' '로 합쳐서 출력한다.
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        # 같은 숫자 중복 제거
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()