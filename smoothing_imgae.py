import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel=kernal)
blur = cv2.blur(img, (5, 5))


titles = ['image', "dst","blur"]
images = [img, dst, blur]


for i in range(len(titles)):
    plt.subplot(1, len(titles), i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()