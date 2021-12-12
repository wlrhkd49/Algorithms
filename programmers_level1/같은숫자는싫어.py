def solution(arr):
    answer = [arr[0]]
    x = arr[0]
    for i in range(1, len(arr)):
        if x != arr[i]:
            x = arr[i]
            answer.append(arr[i])
    return answer