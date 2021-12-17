n, m = map(int, input().split())
arr = [] 

def dfs(a):
    if len(arr) == m:
        # arr을 ' '로 합쳐서 출력한다.
        print(' '.join(map(str, arr)))
        return
    
    # start부터 n까지의 숫자만 사용한다.
    for i in range(a, n+1):
        # 같은 숫자 중복 제거
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()

dfs(1)