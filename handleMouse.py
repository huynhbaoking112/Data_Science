import numpy as np
import cv2


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_CTRLKEY) :
        print(x,", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (x, y, 0), 4)
        cv2.imshow("image", img)

img = np.zeros((512, 512,3), np.uint8)
cv2.imshow("image", img)

cv2.setMouseCallback("image", click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()