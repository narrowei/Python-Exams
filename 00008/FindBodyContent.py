import re

f = open('test.html')
contents = f.readlines()
flag = 0
res = []
for content in contents:
    if re.findall(r'<body>', content) != []:
        flag = 1
    elif re.findall(r'</body>', content) != []:
        flag = 0
    elif flag == 1:
        res.append(content)
print res

