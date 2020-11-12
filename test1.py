# https://auth0.com/blog/image-processing-in-python-with-pillow/

from PIL import Image

image = Image.open('img.jpg')

# image.show() # open in imagebrower

# The file format of the source file.
print(image.format) # Output: JPEG

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: (1200, 776)

# Colour palette table, if any.
print(image.palette) # Output: None

# image.save('new_image.png') # save it with new name and extinsion

# new_image = image.resize((400, 400))
# new_image.save('image_400.jpg')

# resize maintaining aspect ratio
# image.thumbnail((400, 400))
# image.save('image_thumbnail.jpg')