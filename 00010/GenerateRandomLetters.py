import string, random, Image, ImageDraw, ImageFont


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_color():
    color = ['black', 'red', 'green', 'blue', 'gray']
    return random.choice(color)

def random_point(x, y):
    return (random.choice(range(1,x)), random.choice(range(1,y)))

im = Image.new("RGB", (200, 80), "white")
texts = random_char(4)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("angelina.TTF", 70)
front_x = 25
front_y = 20
for i in range(300):
    draw.point(( random.choice(range(1,200)), random.choice(range(1,100))),'black')
for i in range(10):
    draw.line([random_point(200, 80),random_point(200, 80)],'black')
for text in texts:
    text_size = draw.textsize(text, font=font)
    draw.text((front_x, 5), text, random_color(), font=font)
    front_x = front_x + text_size[0] + 5

im.save('new.png')
print random.choice(range(1,200))
print texts

