"""
Phát hiện đường viền là gì?
Phát hiện đường viền (Contour Detection) là một kỹ thuật trong xử lý ảnh được sử dụng để xác định và vạch ra biên giới của các vật thể trong ảnh. Đường viền là một đường cong nối các điểm liền kề nhau dọc theo biên của các vùng có cường độ tương tự trong ảnh. Nó giúp xác định hình dạng của các đối tượng và được dùng nhiều trong các ứng dụng như nhận dạng vật thể, phân tích hình dạng, và thị giác máy tính.

Ứng dụng thực tế của phát hiện đường viền:
Nhận dạng vật thể: Phát hiện hình dạng của các vật thể trong ảnh như hình tròn, hình vuông, v.v.
Phân tích hình dáng đối tượng: Xác định diện tích, chu vi, và các thuộc tính khác của đối tượng.
Theo dõi đối tượng: Giúp xác định và theo dõi đối tượng trong các chuỗi video.
Phân đoạn ảnh: Chia ảnh thành các vùng khác nhau dựa trên đường viền.
Nhận dạng ký tự quang học (OCR): Phát hiện biên giới của các ký tự để nhận dạng chữ.
Cách hoạt động:
Chuyển đổi sang ảnh nhị phân: Đường viền chỉ có thể được phát hiện chính xác trên ảnh nhị phân (ảnh chỉ có giá trị 0 hoặc 255). Do đó, ảnh cần được chuyển đổi sang ảnh nhị phân bằng các phương pháp như ngưỡng (thresholding) hoặc phát hiện cạnh bằng phương pháp Canny.

Phát hiện đường viền: Sau khi có ảnh nhị phân, thuật toán phát hiện đường viền (như cv2.findContours) sẽ tìm các đường viền của các đối tượng trong ảnh.

Cách xây dựng phát hiện đường viền với cv2.findContours trong OpenCV:
Cú pháp của cv2.findContours:
python
Sao chép mã
contours, hierarchy = cv2.findContours(image, mode, method)
image: Ảnh đầu vào (ảnh nhị phân). Đường viền sẽ được phát hiện từ đây.
mode: Chế độ tìm đường viền, ví dụ:
cv2.RETR_EXTERNAL: Chỉ lấy các đường viền ngoài cùng.
cv2.RETR_TREE: Lấy tất cả các đường viền và xây dựng hệ thống phân cấp (hierarchy).
cv2.RETR_LIST: Lấy tất cả các đường viền mà không có hệ thống phân cấp.
method: Phương pháp xấp xỉ đường viền, ví dụ:
cv2.CHAIN_APPROX_SIMPLE: Xấp xỉ đường viền bằng cách loại bỏ các điểm thừa (chỉ lưu các điểm cần thiết).
cv2.CHAIN_APPROX_NONE: Lưu tất cả các điểm trên đường viền (không loại bỏ điểm thừa).
Các bước thực hiện phát hiện đường viền:
1. Đọc ảnh và chuyển đổi sang ảnh nhị phân:
Trước khi phát hiện đường viền, bạn cần chuyển đổi ảnh màu sang ảnh nhị phân.

python
Sao chép mã
import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('image.jpg')

# Chuyển ảnh thành grayscale (ảnh xám)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Áp dụng ngưỡng để chuyển ảnh thành nhị phân
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
2. Phát hiện đường viền bằng cv2.findContours:
Sau khi chuyển sang ảnh nhị phân, bạn có thể sử dụng findContours để phát hiện các đường viền trong ảnh.

python
Sao chép mã
# Phát hiện đường viền
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours: Đây là danh sách các đường viền được phát hiện. Mỗi đường viền là một mảng các điểm tọa độ (x, y).
hierarchy: Đây là hệ thống phân cấp của các đường viền (nếu dùng RETR_TREE).
3. Vẽ đường viền lên ảnh gốc:
Bạn có thể vẽ các đường viền đã phát hiện lên ảnh ban đầu để hiển thị kết quả.

python
Sao chép mã
# Vẽ các đường viền lên ảnh gốc
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Hiển thị ảnh với đường viền
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
-1: Tham số này có nghĩa là vẽ tất cả các đường viền. Nếu muốn vẽ đường viền cụ thể, bạn có thể thay -1 bằng chỉ số của đường viền trong danh sách contours.
(0, 255, 0): Màu của đường viền (xanh lá cây trong hệ màu BGR).
2: Độ dày của đường viền.
Ví dụ hoàn chỉnh:
python
Sao chép mã
import cv2

# Đọc ảnh
image = cv2.imread('image.jpg')

# Chuyển ảnh thành grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Chuyển thành ảnh nhị phân (bằng thresholding)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Tìm đường viền
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ các đường viền lên ảnh gốc
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Hiển thị ảnh kết quả
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
Các thông số và cách dùng cv2.findContours:
cv2.RETR_EXTERNAL: Chỉ lấy các đường viền ngoài cùng (bỏ qua các đường viền bên trong).
cv2.RETR_TREE: Lấy tất cả các đường viền và xây dựng hệ thống phân cấp. Dùng khi cần biết quan hệ cha con giữa các đường viền.
cv2.CHAIN_APPROX_SIMPLE: Phương pháp xấp xỉ để giảm bớt số điểm lưu trữ, chỉ lưu lại các điểm quan trọng.
cv2.CHAIN_APPROX_NONE: Lưu tất cả các điểm trên đường viền, không xấp xỉ.
Ứng dụng thực tế của phát hiện đường viền:
Nhận dạng vật thể: Dùng để xác định các vật thể trong ảnh và đếm số lượng.
Theo dõi đối tượng: Dùng để theo dõi chuyển động của các vật thể trong chuỗi video.
Phân tích hình dạng: Dùng để xác định hình dạng, tính toán chu vi, diện tích của các vật thể.
Phân đoạn ảnh: Chia ảnh thành các phần tương ứng với các vật thể hoặc vùng cụ thể.
Phân tích cấu trúc tế bào: Dùng trong y học để phân tích hình ảnh của tế bào và mô.
Phát hiện đường viền là một công cụ mạnh mẽ trong xử lý ảnh, đặc biệt khi bạn cần xác định và phân tích hình dạng của các đối tượng trong ảnh.
"""
import cv2
import numpy as np

img = cv2.imread("opencv-logo.png",0)
img2 = cv2.imread("opencv-logo.png")

_ , thres = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("thres", thres)


# _ , thres2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("thres2", thres2)
# img3 = cv2.dilate(thres2, (3,3), iterations=5)
# cv2.imshow("img3", img3)

contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy2 = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


cv2.drawContours(img2, contours, -1, (0, 255, 0), 2)
cv2.imshow("Con", img2)




cv2.waitKey(0)
cv2.destroyAllWindows()