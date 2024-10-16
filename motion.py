import cv2 as cv

# Mở video
video = cv.VideoCapture("people.mp4")

# Tạo bộ trừ nền
subtractor = cv.createBackgroundSubtractorMOG2(0, 0)

# Khởi tạo bộ đếm
count = 0

# Xác định vị trí của vùng kiểm tra (dòng ngang)
region_y = 300  # Vị trí y của đường kiểm tra (cần điều chỉnh theo video)
region_thickness = 1
  # Độ dày của đường

# Danh sách các đối tượng đã đi qua vùng kiểm tra
tracked_centroids = []

while True:
    ret, frame = video.read()

    if not ret:
        video = cv.VideoCapture("people.mp4")
        continue

    # Áp dụng trừ nền
    mask = subtractor.apply(frame)

    # Lọc các đối tượng để giảm nhiễu
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, (5, 5))

    # Tìm các đường biên của các đối tượng trong mặt nạ
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Vẽ đường kiểm tra trên khung hình gốc
    cv.line(frame, (0, region_y), (frame.shape[1], region_y), (0, 255, 0), region_thickness)

    # Danh sách để lưu các centroid của khung hiện tại
    current_centroids = []

    for contour in contours:
        # Bỏ qua các đối tượng nhỏ để giảm nhiễu
        if cv.contourArea(contour) < 1000:
            continue

        # Lấy hình chữ nhật bao quanh đối tượng
        x, y, w, h = cv.boundingRect(contour)

        # Tính tọa độ trung tâm của đối tượng
        centroid_x = int(x + w / 2)
        centroid_y = int(y + h / 2)
        current_centroids.append((centroid_x, centroid_y))

        # Vẽ hình chữ nhật bao quanh đối tượng
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Kiểm tra nếu một đối tượng đi qua đường kiểm tra
    for centroid in current_centroids:
        if region_y - region_thickness < centroid[1] < region_y + region_thickness:
            # Kiểm tra nếu đối tượng này chưa được đếm trước đó
            if centroid not in tracked_centroids:
                count += 1
                tracked_centroids.append(centroid)

    # Hiển thị bộ đếm trên khung hình
    cv.putText(frame, f"Count: {count}", (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Hiển thị khung hình
    cv.imshow('Frame', frame)

    # Thoát khi nhấn phím 'X'
    if cv.waitKey(5) == ord('x'):
        break

# Giải phóng tài nguyên
cv.destroyAllWindows()
video.release()
