import cv2
import numpy as np


img1 = np.zeros((236, 236, 3), np.uint8)
img1 = cv2.rectangle(img1, (50,50), (100,100), (255,255,255), -1)
img2 = cv2.imread("test2.jpg")


# img3 = cv2.bitwise_and(img1, img2)
img3 = cv2.bitwise_or(img1, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)


cv2.waitKey(0)
cv2.destroyAllWindows() 