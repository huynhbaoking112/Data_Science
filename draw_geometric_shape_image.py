import cv2
import numpy as np


img = cv2.imread("test2.jpg")



#Ve duong thang
img = cv2.line(img, (0,0), (255, 255), (255, 0, 0), 2)
img = cv2.rectangle(img, (0,0), (50,50), (255, 0, 0), 1)
img = cv2.circle(img, (125,125), 25, (255,0,0), 1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "king", (0,20), font, 1, (255,0,0),4)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()