def solution(array, commands):
    answer = []
    for i in commands:
        x = i[0]-1
        y = i[1]
        z = i[2]-1
        new_array = array[x:y]
        new_array.sort()
        answer.append(new_array[z])

    return answer