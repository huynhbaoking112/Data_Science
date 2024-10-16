import numpy as np
import cv2 as cv





def nothing(x):
    print(x)



img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image")
cv.createTrackbar("B", "image", 0, 255, nothing)
cv.createTrackbar("G", "image", 0, 255, nothing)
cv.createTrackbar("R", "image", 0, 255, nothing)

switch  = 'O : OFF\n 1 : ON'
cv.createTrackbar(switch, "image", 0, 1, nothing)



# def testMouse(event, x, y, flags, params):
#     if event == cv.EVENT_LBUTTONDOWN:
#         print("king")
#         cv.putText(img, f"{x}, {y}", (x, y), cv.FONT_HERSHEY_SIMPLEX, 3, (x, y, 0), 3)

# cv.setMouseCallback("image", testMouse)


while True:
    cv.imshow('image', img)
    k= cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos("B", "image")
    g = cv.getTrackbarPos("G", "image")
    r = cv.getTrackbarPos("R", "image")
    s = cv.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = 0
    else :
        img[:] = (b,g,r)
    

cv.destroyAllWindows()