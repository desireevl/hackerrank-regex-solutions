import re

n_lines = int(input())
count = 0

for i in range(n_lines):
    line = input()
    match = re.search(r'hackerrank', line, re.IGNORECASE)

    if match:
        count += 1

print(count)
