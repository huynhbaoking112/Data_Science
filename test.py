import cv2

video = cv2.VideoCapture("cars.mp4")


back_sub = cv2.createBackgroundSubtractorMOG2()
b = cv2.createBackgroundSubtractorKNN()



while video.isOpened():

    ret, frame = video.read()

    # frame2 = back_sub.apply(frame)
    frame2 = b.apply(frame)

    cv2.imshow("t", frame2)
    # cv2.imshow("s", frame2s)

    _ , frame3 = cv2.threshold(frame2, 150, 255, cv2.THRESH_BINARY)
    frame3= cv2.erode(frame3, None)
    frame3= cv2.dilate(frame3, None)

    contours, _ = cv2.findContours(frame3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
              (x, y, w, h) = cv2.boundingRect(contour) 

              if cv2.contourArea(contour) > 500:
                cv2.rectangle(frame, (x,y),(x+w, y+h),(0, 255, 0), 2) 

    cv2.imshow("frame", frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
     break




video.release()
cv2.destroyAllWindows()