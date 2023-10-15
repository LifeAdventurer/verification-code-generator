from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import numpy as np
import matplotlib.pyplot as plt

width, height = 200, 100
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size = 60)

chars = [str(np.random.randint(0, 10)) for _ in range(4)]

points = 50
x_points = np.linspace(0, width, points)
y_points = np.sin(x_points / 100) * 20

for i, char in enumerate(chars):

  distortion = random.uniform(0.8, 2)
  shear_x = random.uniform(-0.2, 0.2)
  shear_y = random.uniform(-0.3, 0.3)
  x = int(x_points[i * (points // 4)])
  y = int(y_points[i * (points // 4)])

  char_width, char_height = font.getsize(char)
  char_image = Image.new('RGBA', (char_width, char_height), (255, 255, 255, 0))
  char_draw = ImageDraw.Draw(char_image)
  char_draw.text((0, 0), char, fill = 'black', font = font)

  char_image = char_image.transform(char_image.size, Image.AFFINE, (1, shear_x, 0, shear_y, 1, 0))
  char_image = char_image.resize((int(char_width * distortion), int(char_height)))

  image.paste(char_image, (x, y), char_image)

for _ in range(100):
  x1 = np.random.randint(0, width)
  y1 = np.random.randint(0, height)
  x2 = np.random.randint(0, width)
  y2 = np.random.randint(0, height)
  draw.line([(x1, y1), (x2, y2)], fill = 'black')

image_array = np.array(image)

random_array = np.random.randint(0, 256, size=(height, width, 3), dtype = np.uint8)

image_array += random_array

blurred_image_array = image.filter(ImageFilter.GaussianBlur(radius = 2))

plt.imshow(blurred_image_array)
plt.axis('off')
plt.show()
