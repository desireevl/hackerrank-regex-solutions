import re

n_lines = int(input())

for i in range(n_lines):
    line = input()
    match = re.search(r'^[hH][iI]\s[^Dd]', line)

    if match:
        print(line)
    else:
        None
