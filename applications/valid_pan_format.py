import re

n_lines = int(input())

for i in range(n_lines):
    line = input()
    match = re.search(r'^[A-Z]{5}\d{4}[A-Z]$', line)

    if match:
        print('YES')
    else:
        print('NO')
