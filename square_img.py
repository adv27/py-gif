import os
import sys
from PIL import Image
import imageio
import numpy
import time
import image_slicer


def get_square(w, h):
    return (w, w) if w >= h else (h, h)


def get_square_image(img):
    img_w, img_h = img.size
    square = get_square(img_w + 50, img_h)
    with Image.new('RGB', square, (255, 255, 255)) as background:
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        frame = img.convert('RGB')
        background.paste(frame, offset)
        return numpy.asarray(background)


def main():
    try:
        img_path = sys.argv[1]
    except IndexError:
        print('Please provide image path!')
        return
    if os.path.isfile(img_path):
        with Image.open(img_path) as img:
            print(img.size)
            square_image = get_square_image(img)
            _, file_extension = os.path.splitext(img_path)
            filename = os.path.basename(img_path)
            output_uri = os.path.join(
                os.path.dirname(img_path), '{}_square.{}'.format(
                    filename,
                    file_extension
                )
            )
            imageio.imwrite(output_uri, square_image)

            # slice the image
            slices = image_slicer.slice(output_uri, 2, save=False)
            for index, s in enumerate(slices):
                image = s.image
                image = image.convert('RGB')
                output_uri = os.path.join(
                    os.path.dirname(img_path), 'slice_{}.{}'.format(
                        index,
                        file_extension
                    )
                )
                #convert image to numpy array then save to file
                imageio.imwrite(output_uri, numpy.asarray(image))
    else:
        print('File not found!')


if __name__ == '__main__':
    main()
