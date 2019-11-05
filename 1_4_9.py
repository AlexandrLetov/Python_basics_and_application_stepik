count = int(input())
namespases = {'global': 'None'}
variables = {'global': set()}


def create(namespase, var):
    namespases[namespase] = var
    variables[namespase] = set()


def add(namespase, var):
    variables[namespase].add(var)


def get(namespase, var):
    if var in variables[namespase]:
        print(namespase)
    elif namespases[namespase] != 'None':
        get(namespases[namespase], var)
    else:
        print(None)


for i in range(count):
    command, namespase, var = input().split(' ')
    if command == 'create':
        create(namespase, var)
    if command == 'add':
        add(namespase, var)
    if command == 'get':
        get(namespase, var)
