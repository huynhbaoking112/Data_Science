import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cancuoc.jpg', 0)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelXY = cv2.bitwise_or(sobelX, sobelY)


titles = ['image',"lap","sobelX","sobelY", "sobelXY"]
images = [img, lap, sobelX, sobelY, sobelXY]


for i in range(len(titles)):
    plt.subplot(len(titles),1 , i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()