import sys
import re

pattern = r'human'
result = r'computer'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, result, line))
    
