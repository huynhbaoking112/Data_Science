import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test2.jpg', 0)
canny = cv2.Canny(img, 100, 200)


titles = ['image',"canny"]
images = [img,canny]


for i in range(len(titles)):
    plt.subplot(len(titles),1 , i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()