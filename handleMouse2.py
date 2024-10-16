import numpy as np
import cv2


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)



# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN :
        

#         if  len(points) != 0:
#             cv2.line(img, (x,y), points[-1], (x+1,y+1,0),2)

#         points.append((x,y))
#         cv2.circle(img, (x, y), 3, (x, y, 0), -1)

#         cv2.imshow("image", img)

# img = np.zeros((512, 512,3), np.uint8)
# cv2.imshow("image", img)

# points = []

# cv2.setMouseCallback("image", click_event)


# cv2.waitKey(0)
# cv2.destroyAllWindows()






def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :
        blue = img[ x, y, 0]
        green = img[ x, y, 1]
        red = img[ x, y, 2]

        # cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)
        cv2.imshow("image2", mycolorImage)

        mycolorImage[:] = [blue, green, red]
        cv2.imshow("image2", mycolorImage)
        cv2.imshow("image", img)
    

img = cv2.imread("test2.jpg")

cv2.imshow("image", img)



cv2.setMouseCallback("image", click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()