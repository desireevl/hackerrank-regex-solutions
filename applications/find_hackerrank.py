import re

n_lines = int(input())

for i in range(n_lines):
    line = input()
    match1 = re.search(r'^(hackerrank)', line)
    match2 = re.search(r'(hackerrank)$', line)
    match3 = re.search(r'^(hackerrank)$', line)

    if match3:
        print(0)
    elif match1:
        print(1)
    elif match2:
        print(2)
    else:
        print(-1)
