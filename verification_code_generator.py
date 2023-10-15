from PIL import Image, ImageDraw, ImageFont, ImageFilter
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
  x = int(x_points[i * (points // 4)])
  y = int(y_points[i * (points // 4)])
  draw.text((x, y), char, fill = 'black', font = font)

for _ in range(50):
  x1 = np.random.randint(0, width)
  y1 = np.random.randint(0, height)
  x2 = np.random.randint(0, width)
  y2 = np.random.randint(0, height)
  draw.line([(x1, y1), (x2, y2)], fill = 'black')
  
image_array = np.array(image)

blurred_image_array = image.filter(ImageFilter.GaussianBlur(radius = 2))

plt.imshow(blurred_image_array)
plt.axis('off')
plt.show()
