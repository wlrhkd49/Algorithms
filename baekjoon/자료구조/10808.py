alpha = [0] * 26
for i in input():
    index = ord(i) - ord('a')
    alpha[index] += 1
    
for a in alpha:
    print(a, end=' ')
