import sys
import re

pattern = r'(\w)(\1+)'
result = r'\1'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, result, line))
