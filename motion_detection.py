import cv2

video = cv2.VideoCapture("cars.mp4")


status1, frame1 = video.read()
status2, frame2 = video.read()


while video.isOpened():

        gray = cv2.absdiff(frame1,frame2)
    
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (5,5), 0)

        _ , thres3 = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

        dilation = cv2.dilate(thres3, None, iterations=3)

        
        # cv2.imshow("king", thres3)
        # cv2.imshow("dilation", dilation)
        # cv2.imshow("gray", gray)
        # cv2.imshow("gray", frame1)

        contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

      
        for i, contour in enumerate(contours):
              (x, y, w, h) = cv2.boundingRect(contour) 

              if cv2.contourArea(contour) > 700:
                cv2.rectangle(frame1, (x,y),(x+w, y+h),(0, 255, 0), 2) 

             
             

        cv2.imshow("frame", frame1)

        frame1 = frame2

        ret ,frame2 = video.read()


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
   




video.release()
cv2.destroyAllWindows()