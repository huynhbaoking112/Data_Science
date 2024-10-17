import cv2
from matplotlib  import pyplot as plt
import numpy as np



img = cv2.imread("banh.png", 0)
goc = cv2.imread("banh.png")

_, mask2 = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((3,3), np.uint8)
dilation = cv2.dilate(mask2, kernal, iterations=2)

saudilation = cv2.bitwise_and(goc, goc,mask=dilation)



titles = ['image',"goc", "mask2", "dilation", "saudilation"]
images = [img ,goc, mask2, dilation,saudilation]

for i in range(len(titles)):
    plt.subplot(1, len(titles), i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey(0) 
cv2.destroyAllWindows()