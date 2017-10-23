# -*- coding: UTF-8 -*-
import re

with open("text") as f:
    s = f.readlines()
    print s
#text = raw_input("请输入字符串：")
# m = re.match(r'(\d*)(\s*)(\w*)',text,)
#
# print m.group(0),m.group(1),m.group(2),m.group(3)

m = re.match(r'([0-9]*)([\s\;]*)(\w*)',s[1],)
print m.group(0),m.group(1),m.group(2),m.group(3)