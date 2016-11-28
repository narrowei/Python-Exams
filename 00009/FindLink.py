import re

import re

f = open('test.html')
contents = f.readlines()
links = []
for content in contents:
    link = re.findall(r'(?<=href=")[^"]+', content)
    if link != []:
        links.append(link)

print links