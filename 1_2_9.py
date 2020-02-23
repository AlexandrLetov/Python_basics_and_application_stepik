#через is так и не получилось решить.
ans = 0
while len(objects) != 0:
    x = objects[len(objects)-1]
    objects.pop()
    if x not in objects:
        ans += 1
print(ans)