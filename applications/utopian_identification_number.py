import re

n_lines = int(input())

for i in range(n_lines):
    line = input()
    match = re.search(r'^[a-z]{,3}\d{2,8}[A-Z]{3,}', line)

    if match:
        print('VALID')
    else:
        print('INVALID')
