import cv2
import datetime

cap = cv2.VideoCapture(0)

# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

# print(cap.get(3))
# print(cap.get(4))
cap.set(3, 1208)
cap.set(4, 720)



while cap.isOpened():
    
    ret, frame = cap.read()

    if ret == True:
        
        text = f"{datetime.datetime.now()}"

        frame = cv2.putText(frame, text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0 ,0), 5)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()