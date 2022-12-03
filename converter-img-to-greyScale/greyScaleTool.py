from PIL import Image
img = Image.open('image.png').convert('L')
img.save('greyscale.png')
