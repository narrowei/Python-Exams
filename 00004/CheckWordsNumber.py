import re
import csv

content = open('words.txt').read()
words = re.split(r'[^a-zA-Z-]+',content)
res = {}
for word in words:
    if res.has_key(word):
        res[word] += 1
    else:
        res[word] = 1
result = csv.writer(open('result.csv','wb'))
result.writerow(['word','num'])
for i in res:
    tmp = [i,res[i]]
    result.writerow(tmp)
