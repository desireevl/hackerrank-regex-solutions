import re

n_lines = int(input())

for i in range(n_lines):
    line = input()
    m = re.match(r"(?P<countrycode>^\d+)(-|\s)(?P<localcode>\d+)(-|\s)(?P<number>\d+)", line)
    
    print("CountryCode={0},LocalAreaCode={1},Number={2}".format(m.group('countrycode'),m.group('localcode'),m.group('number')))
