data = input()
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1

steps = { (-2,-1), (-2,1), (1,-2), (1,2), (-1,-2), (-1,2), (2,-1), (2,1)}

result = 0
for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if(next_x<1 or next_x>8 or next_y<1 or next_y>8):
        continue
    result+=1

print(result)