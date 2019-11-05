# Когда-нибудь доделаю. Люблю тесты степика.

n = int(input())
parents = {}  # Ключ - потомок, значения - родители

for i in range(n):
    line = input()
    if line.find(' ') == -1:
        parents[line] = None
    else:
        parents[line[:line.find(' ')]] = line[line.find(':')+2:].split(' ')
# print(parents)

for key in parents.keys():
    if parents[key] is not None:
        for item in parents[key]:
            if parents[item] is not None:
                for value in parents[item]:
                    if value not in parents[key]:
                        parents[key].append(value)

# print(parents)

m = int(input())

exception_list = []
was = []
for i in range(m):
    exception = input()
    if exception not in was:
        was.append(exception)
        for key in parents.keys():
            if parents[key] is not None:
                if exception in parents[key]:
                    if key not in exception_list:
                        exception_list.append(key)
        parents.pop(exception)
for item in exception_list:
    print(item)
