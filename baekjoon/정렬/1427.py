data = []
for i in str(int(input())):
	data.append(i)

data.sort(reverse = True)

print("".join(data))