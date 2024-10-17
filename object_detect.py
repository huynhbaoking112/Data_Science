import cv2
import numpy as np

def nothing(x):
    pass


cv2.namedWindow("tracking")
cv2.createTrackbar("LH", "tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "tracking", 255, 255, nothing)
cv2.createTrackbar("US", "tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "tracking", 255, 255, nothing)


cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()


    #Chuyển sang HSV để dễ dàng nhận biết màu thông qua độ bão hòa và độ sáng
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Giới hạn dưới và giới hạn trên của màu xanh lam
    l_b =np.array([cv2.getTrackbarPos("LH", "tracking"), cv2.getTrackbarPos("LS", "tracking"), cv2.getTrackbarPos("LV", "tracking")])
    u_b = np.array([ cv2.getTrackbarPos("UH", "tracking"),  cv2.getTrackbarPos("US", "tracking"),  cv2.getTrackbarPos("UV", "tracking")])


    #lọc ra các khoảng đã định
    mask = cv2.inRange(hsv, l_b, u_b)

    #áp dụng mặt nạ lên ảnh gốc để chỉ giữ lại các vùng có màu xanh lam
    res = cv2.bitwise_and(frame,frame, mask=mask)


    cv2.imshow("video", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

     
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()


# import numpy as np
# import cv2

# green = np.uint8([[[0, 255, 0]]]) # Here insert the BGR values which you want to convert to HSV
# hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print(hsvGreen)

# lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
# upperLimit = hsvGreen[0][0][0] + 10, 255, 255

# print(lowerLimit)
# print(upperLimit)