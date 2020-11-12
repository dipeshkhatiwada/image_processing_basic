from PIL import Image

image = Image.open('img.jpg')

box = (10, 20, 300, 400)
# (left, upper, right, lower)
cropped_image = image.crop(box)
cropped_image.save('cropped_image.jpg')