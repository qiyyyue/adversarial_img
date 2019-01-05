from urllib.request import urlretrieve

import PIL.Image as image
import numpy as np


url = "http://www.anishathalye.com/media/2017/07/25/cat.jpg"
img_path, _ = urlretrieve(url)
img_class = 281
img = image.open(img_path)

print(np.array(img).shape)