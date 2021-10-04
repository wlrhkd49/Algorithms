data = []
for i in range(int(input())):
	s = input()
	if s in data:
		continue
	data.append(s)

data.sort(key = lambda x : (len(x), x))

for d in data:
	print(d)