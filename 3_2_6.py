s, a, b = (input() for i in range(3))

count = 0

if a in b and a in s:
    print('Impossible')
else:
    while a in s:
        count += 1
        s = s.replace(a, b)
    print(count)
