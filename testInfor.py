import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cancuoc.jpg', 0)
_ , img2 = cv2.threshold(img, 115, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)

opening =cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, kernel)



cv2.imshow("anh",opening)







cv2.waitKey(0)
cv2.destroyAllWindows()
