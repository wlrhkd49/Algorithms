data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
x = input()

for a in data:
    x = x.replace(a, '$')

print(len(x))