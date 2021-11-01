import re

import io
import sys
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

s = input_stream.readlines()
s = "\n".join(s)

pc = '(//.*|/\*[\d\D]*?\*/)'
mc = re.findall(pc, s)
for v in mc:
    vs = v.split("\n\n")
    for l in vs:
        print (l.lstrip())
