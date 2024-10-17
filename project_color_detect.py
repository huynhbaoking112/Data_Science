import cv2 as cv
import webcolors
import math

cap = cv.VideoCapture(0)
 

def xacDinhMau(r, g, b):
    doLech = {}
    for name in webcolors.names("html4"):
        
        r2, g2, b2 = webcolors.name_to_rgb(name)

        Eculi = math.sqrt((r2-r)**2 + (g2-g)**2 + (b2 - b)**2)

        doLech[Eculi] = name

    return doLech[min(doLech.keys())]




while cap.isOpened():

    ret, frame = cap.read()


    
    # print(frame.shape) (240, 320)

    #mau tam BGR
    (b, g, r) = frame[240, 320] 
    b, g, r = int(b),int(g), int(r)

    #khung tron tam
    cv.circle(frame, (320, 240), 5, (250, 255, 255), 2)
    cv.circle(frame, (320, 240), 25, (250, 255, 255), 1)

    #lay ten mau
    text = xacDinhMau(r, g, b)
    cv.putText(frame, text, (300, 60), cv.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 3)

    #show video
    cv.imshow("video", frame)


    if cv.waitKey(1) & 0xFF == ord("q"):
        break




cap.release()
cv.destroyAllWindows()