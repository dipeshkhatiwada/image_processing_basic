from PIL import Image

image = Image.open('img.jpg')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_image.jpg')