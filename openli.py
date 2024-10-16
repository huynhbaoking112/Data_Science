import cv2


# neu muon doc tu file thi dien file
# cap = cv2.VideoCapture("people.mp4")
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))


while cap.isOpened() :
# doc tu khung nhin lien tuc
    ret, frame = cap.read()

    if ret == True:

    #lay ty le khung hinh
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #chuyen doi thang mau thanh xam 
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #ghi khung hinh
        out.write(frame)
        
    #hien thi khung nhin
        # cv2.imshow('frame', gray)
        cv2.imshow('frame', frame)


    #cho 1 ms de lang nghe phim tat tu nguoi dung
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release() 
out.release()
cv2.destroyAllWindows()