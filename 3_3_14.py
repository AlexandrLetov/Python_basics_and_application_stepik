import sys
import re

pattern = r'\b(\w)(\w)(\w*)\b'
result = r'\2\1\3'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, result, line))
