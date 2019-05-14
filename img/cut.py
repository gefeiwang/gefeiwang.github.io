import imageio
import numpy as np
import PIL.Image

img = np.asarray(PIL.Image.open('HKUST.png').resize((128+32,256)))

img = np.pad(img, [(64,64), (64+32,64+32), (0,0)], 'constant', constant_values=0)

print(np.shape(img))

imageio.imsave('HKUST2.png', img)