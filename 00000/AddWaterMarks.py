import Image
import ImageDraw

def drawNumber(f, number):
  # open file
  img = Image.open(f)
  size = img.size
  draw = ImageDraw.Draw(img)
  text = number
  num_size = draw.textsize(text)
  x_start = size[0]-num_size[0]
  # drawing circle first on the top-right of the picture and its size is changed by the number's size
  draw.ellipse((x_start-5,0,size[0],num_size[0]+5), (255, 0, 0))
  y_start =  (num_size[0]+5)/2 - num_size[1]/2
  # writing the number on the center of the circle
  draw.text((x_start-2, y_start), text, (255, 255, 255))
  img.save(f)
  del (img, draw)

drawNumber('img/header.png', '28')
