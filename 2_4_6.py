import os

result = []
os.chdir('./Data/')
for current_dir, dirs, files in os.walk('.'):
    for file in files:
        if file[-3:] == '.py':
            if current_dir[2:] not in result:
                result.append(current_dir[2:])

for _dir in sorted(result)
    print(_dir)