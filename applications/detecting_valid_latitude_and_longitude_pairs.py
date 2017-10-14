#Python2 solution

import re

r = re.compile(r"[(][+-]?(([0-8]\d?(\.\d+)?)|(90(\.0+)?)), [+-]?(((\d|1[0-7])\d(\.\d+)?)|(180(\.0+)?))[)]")

for i in range(input()):
    if(r.match(raw_input())):
       print 'Valid'
    else :
       print 'Invalid'
