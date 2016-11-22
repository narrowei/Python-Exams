import re
import os

def countWords(content):
    words = re.split(r'[^a-zA-Z-]+',content)
    res = {}
    for word in words:
        if res.has_key(word):
            res[word] += 1
        else:
            res[word] = 1
    return res


diaries = os.listdir('diary')
for diary in diaries:
    f = open('diary/'+diary)
    title = f.readline()
    title = re.split(r'[^a-zA-z]+', title)
    res = countWords(f.read())
    #res = sorted(res.iteritems(), key=lambda d: d[1], reverse=True)
    tmp = {}
    for keyword in title:
        if res.has_key(keyword):
            tmp[keyword] = res[keyword]
    tmp = sorted(tmp.iteritems(), key=lambda d: d[1], reverse=True)
    keywords = []
    for word in tmp:
         KW = re.findall(r'[A-Z]+[a-z]*', word[0])
         if KW != []:
             keywords.append(KW)
    print keywords