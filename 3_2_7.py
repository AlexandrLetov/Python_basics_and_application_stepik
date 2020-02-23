s, t = (input() for i in range(2))
pos = 0
result = 0
while len(s[pos:]) >= len(t):
    if s[pos:].startswith(t):
        result += 1
    pos += 1

print(result)