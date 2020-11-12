# https://auth0.com/blog/image-processing-in-python-with-pillow/

from PIL import Image

image = Image.open('img.jpg')

image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
# Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM, 
# Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270 or Image.TRANSPOSE.
image_flip.save('image_flip.jpg')