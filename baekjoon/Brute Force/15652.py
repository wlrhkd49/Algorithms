n, m = map(int, input().split())
arr = [] 

def dfs(a):
    if len(arr) == m:
        # arr을 ' '로 합쳐서 출력한다.
        print(' '.join(map(str, arr)))
        return
    
    for i in range(a, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)
