from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
# print(img.size)
img.thumbnail((400, 400))
img.save('thumbnail.jpg')

print(img.size)