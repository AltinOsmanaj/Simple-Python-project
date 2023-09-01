from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))	

# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)


# filtered_img.save('blur.png', 'png')
# filtered_img.save('smooth.png', 'png')
# filtered_img.save('sharpen.png', 'png')

# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(180)
# filtered_img.save('grey.png', 'png')
# crooked.save('grey.png', 'png')
# filtered_img.show()

# resize = filtered_img.resize((300, 300))
# resize.save('grey.png', 'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('grey.png', 'png')