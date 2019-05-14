import imageio
import numpy as np
import PIL.Image

img = np.asarray(PIL.Image.open('700x700.png').resize((700,700)))

# img = np.pad(img, [(64,64), (64+32,64+32), (0,0)], 'constant', constant_values=0)

# print(np.shape(img))

imageio.imsave('195x195.png', img)