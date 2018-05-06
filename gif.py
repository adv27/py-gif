#Python 3.6.3

import os
from PIL import Image
import imageio

def get_square(w, h):
  return w if w >= h else h

folder = r'C:\Users\vdanh\Desktop\python\GIF'
name = 'image.gif'

img = Image.open(os.path.join(folder,name))
img_w, img_h = img.size
duration = img.info['duration']
sq = get_square(img_w, img_h)
try:
  img.seek(0)
  while True:
    background = Image.new('RGB', (sq, sq),(255,255,255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    frame = img.convert('RGB')
    background.paste(frame,offset)
    background.save(os.path.join(folder, 'foo{}.png'.format(img.tell())), 'PNG')
    img.seek(img.tell() + 1)            
except EOFError:
  pass

file_names = sorted((fn for fn in os.listdir(folder) if fn.endswith('.png')))
images = []
for fn in file_names:
  images.append(imageio.imread(os.path.join(folder,fn)))
imageio.mimsave(os.path.join(folder,'output.GIF'),images,duration = duration/1000)