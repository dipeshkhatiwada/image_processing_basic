# https://auth0.com/blog/image-processing-in-python-with-pillow/

from PIL import Image

image = Image.open('img.jpg')

image_rot_90 = image.rotate(90)
image_rot_90.save('image_rot_90.jpg')

image_rot_180 = image.rotate(180)
image_rot_180.save('image_rot_180.jpg')

# image.rotate(18).save('image_rot_18.jpg')
# expand the dimensions of the rotated image to fit the entire view
image.rotate(18, expand=True).save('image_rot_18.jpg')