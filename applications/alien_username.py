import re

n_lines = int(input())

for i in range(n_lines):
    line = input()
    match = re.search(r'^(_|\.)[0-9]+[a-zA-Z]*(_)?$', line)

    if match:
        print('VALID')
    else:
        print('INVALID')
