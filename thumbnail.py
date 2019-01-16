from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob(r'data\*.jpg'):
    f, ext = os.path.splitext(infile)
    img = Image.open(infile)
    img.thumbnail(size)
    img.save('{}-thumnnail.{}'.format(f, ext), 'JPEG')
