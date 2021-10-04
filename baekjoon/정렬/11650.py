data = []
for i in range(int(input())):
	x, y = map(int,input().split())
	data.append((x,y))

data.sort(key = lambda x : (x[0], x[1]))

for d in data:
	print(d[0], d[1])