import sys
import re

pattern = r'\b[aA]+\b'
result = r'argh'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, result, line, count=1, flags=re.IGNORECASE))
