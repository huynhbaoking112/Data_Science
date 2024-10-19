import numpy as np
import cv2

img = cv2.imread("shape2.png")
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

_ , thres = cv2.threshold(imgGrey, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    
    #chu vi cua countour 
    chuVi = cv2.arcLength(contour, True)

    #Xu li giam diem nhieu
    vienTinhChinh = cv2.approxPolyDP(contour, chuVi * 0.02, True)

    #ap diem 
    cv2.drawContours(img, [vienTinhChinh], -1, (0, 255, 0), 2)
    x = vienTinhChinh.ravel()[0]
    y = vienTinhChinh.ravel()[1]
    if len(vienTinhChinh) == 3:
        cv2.putText(img, "Tam giac", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
    elif len(vienTinhChinh) == 4:
        x, y, w, h = cv2.boundingRect(vienTinhChinh)
        asp = float(w)/h
        if asp >= 0.95 and asp <= 1.05:
            cv2.putText(img, "Hinh Vuong", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
        else:
            cv2.putText(img, "Chu Nhat", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
    elif len(vienTinhChinh) == 5:
        cv2.putText(img, "Ngu Giac", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
    elif len(vienTinhChinh) == 6:
        cv2.putText(img, "Luc Giac ", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
    elif len(vienTinhChinh) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
    else:
        cv2.putText(img, "Tron", (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)


cv2.imshow("shapes", img)


cv2.waitKey(0)
cv2.destroyAllWindows()