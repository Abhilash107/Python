from sklearn.datasets import load_digits

digits = load_digits()

import matplotlib.pyplot as plt

axes = plt.subplot()# for single 

image = plt.imshow(digits.images[22], cmap = plt.cm.gray_r)
xticks = axes.set_xticks([])
yticks = axes.set_yticks([])
plt.show()
