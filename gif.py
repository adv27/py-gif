#Python 3.6.3

import os
from PIL import Image
import imageio
import numpy
import time

def get_square(w, h):
  return (w, w) if w >= h else (h, h)

def square_frames(image):
    with Image.new('RGB', square,(255,255,255)) as background:
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        try:
            img.seek(0)
            while True:
                frame = img.convert('RGB')
                background.paste(frame, offset)
                yield numpy.asarray(background)
                img.seek(img.tell() + 1)            
        except EOFError:
            pass

folder = r'C:\Users\vdanh\Desktop\python\GIF'
name = 'source.gif'

time_start = time.time()
with Image.open(os.path.join(folder,name)) as img:
    img_w, img_h = img.size
    duration = img.info['duration']
    print('Source info: {}\n{}'.format(img.info, img.size))
    square = get_square(img_w, img_h)

    # images = []
    # try:
    #     background = Image.new('RGB', square,(255,255,255))
    #     bg_w, bg_h = background.size
    #     offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

    #     img.seek(0) #start at 1st frame
    #     while True:
    #         frame = img.convert('RGB')
    #         background.paste(frame,offset)
    #         # background.save(os.path.join(folder, 'foo{}.png'.format(img.tell())), 'PNG')
    #         images.append(numpy.asarray(background))
    #         img.seek(img.tell() + 1)            
    # except EOFError:
    #     pass

    images = square_frames(img)

    with imageio.get_writer(os.path.join(folder,'output.GIF'), mode='I', duration=duration/1000, subrectangles=True) as writer:
        for image in images:
            writer.append_data(image)

with Image.open(os.path.join(folder,'output.GIF')) as im:
    im.info['loop']= 0
    print('Output info: {}\n{}'.format(im.info, im.size))
time_end = time.time()
print('Time taken: {}'.format(time_end - time_start))