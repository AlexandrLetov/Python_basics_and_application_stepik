n = int(input())
parents = {}  # Ключ - потомок, значения - родители

for i in range(n):
    line = input()
    if line.find(' ') == -1:
        parents[line] = None
    else:
        parents[line[:line.find(' ')]] = line[line.find(':')+2:].split(' ')

for key in parents.keys():
    if parents[key] is not None:
        for item in parents[key]:
            if parents[item] is not None:
                for value in parents[item]:
                    if value not in parents[key]:
                        parents[key].append(value)


q = int(input())

for i in range(q):
    parent, child = input().split(' ')
    if parent == child:
        print('Yes')
    elif parents[child] is None:
        print('No')
    elif parent in parents[child]:
        print('Yes')
    else:
        print('No')
