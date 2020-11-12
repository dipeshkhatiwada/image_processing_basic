from PIL import Image

image = Image.open('img.jpg')

logo = Image.open('py.png')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
# image_copy.paste(logo, position) # black bg

#for transparent background
image_copy.paste(logo, position, logo)
image_copy.save('pasted_image.jpg')