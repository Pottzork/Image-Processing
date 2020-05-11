from PIL import Image, ImageFilter

img = Image.open("./Pokedex/covid19.jpg")

img.thumbnail((400, 400))
img.save("Thumbnail.jpg")
print(img.size)

# -----This makes the image blurry----
# filtered_img = img.filter(ImageFilter.BLUR)


# ----This makes makes the image in greyscale----
# filtered_img = img.convert("L")


# ----Resize IMAGE-----
# box = (100,100,400,400)
# region = filtered_img.crop(box)


# If you want to resize the image remember to put it in a tuple
# resize = filtered_img.resize((300,300))
# This saves the image from let's say a jpeg to png
# region.save("grey.png", "png")
