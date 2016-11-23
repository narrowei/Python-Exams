import re,os

files = os.listdir('Code')
for file in files:
    f = open('Code/'+file)
    codes = f.readlines()
    all_line = len(codes)
    count_short_comment = 0
    count_long_comment = 0
    count_blank_line = 0
    flag = 0
    for code in codes:
        short_comment =  re.findall(r'^#.*$',code)
        long_comment = re.findall(r'\'\'\'',code)
        blank_line = re.findall(r'^ *$',code)
        if short_comment != []:
            count_short_comment = count_short_comment + 1
        if long_comment != []:
            if flag == 0:
                flag = 1
            else:
                flag = 0
        else:
            if flag == 1:
                count_long_comment = count_long_comment + 1
        if blank_line != []:
            count_blank_line = count_blank_line + 1
    count_code_line = all_line-count_blank_line-count_long_comment-count_short_comment
    results = {'all_line':all_line,'count_code_line':count_code_line,'count_blank_line':count_blank_line,'count_long_comment':count_long_comment,'count_short_comment':count_short_comment}
    print results