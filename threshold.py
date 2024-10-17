import cv2 as cv


# doc anh voi che do xam - che do xam bao gom 1 gia tri trong tung pixel tuong duong voi 0 - 255 (do sang cua diem anh)
img = cv.imread("test2.jpg", 0)


# threshold 
_,img2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)


cv.imshow("img", img)
cv.imshow("img2", img2)


cv.waitKey(0)
cv.destroyAllWindows()