import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
 


cv.namedWindow("image")
cv.createTrackbar("B","image", 0, 255, nothing)
cv.createTrackbar("N-0/C-1","image", 0, 1, nothing)


imgs = cv.imread("test2.jpg")
while True:

    b = cv.getTrackbarPos("B", "image")
    c = cv.getTrackbarPos("N-0/C-1", "image")
    img = imgs.copy()

  


    if b!= 0:
        cv.putText(img, f"{b}", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 3)
    else:
        cv.putText(img, "", (100, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 3)

     # Chuyển sang màu xám nếu thanh trượt N-0/C-1 là 1
    if c == 1:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # Chuyển lại sang BGR để hiển thị đúng

    cv.imshow("image",img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()




