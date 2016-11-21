import Image
import os


pathDir = os.listdir('pics')
print pathDir
s_x = 640

for pic in pathDir:
    if pic[0] == '.':
        continue
    im = Image.open('pics/'+pic)
    (x,y) = im.size
    s_y = y * s_x / x
    out = im.resize((s_x,s_y),Image.ANTIALIAS)
    out.save('f_pic/'+pic)