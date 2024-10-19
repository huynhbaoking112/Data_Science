"""Template Matching là một kỹ thuật trong xử lý ảnh và thị giác máy tính, dùng để tìm vị trí của một mẫu (template) trong một ảnh lớn hơn. Mục tiêu là xác định khu vực trong ảnh lớn (ảnh gốc) có mức độ giống với mẫu (template) nhất, và sau đó đánh dấu hoặc xử lý khu vực đó.

Cách hoạt động:
Template (mẫu): Đây là một hình ảnh nhỏ mà bạn muốn tìm trong ảnh lớn hơn.
Ảnh gốc: Đây là hình ảnh lớn mà bạn muốn tìm kiếm mẫu trong đó.
Kết quả: Template matching sẽ so sánh mẫu với từng vùng nhỏ trong ảnh gốc, tính toán mức độ tương tự, và trả về vị trí có độ tương đồng cao nhất giữa mẫu và ảnh gốc.
Phương pháp thực hiện:
Có nhiều phương pháp khác nhau để thực hiện template matching, và OpenCV hỗ trợ một số phương pháp thông dụng như:

cv2.TM_SQDIFF: Tính bình phương độ chênh lệch giữa template và ảnh gốc tại mỗi điểm. Giá trị càng nhỏ thì càng giống nhau.
cv2.TM_CCORR: Tương quan trực tiếp giữa mẫu và ảnh gốc.
cv2.TM_CCOEFF: So sánh mức tương quan của các pixel với mức trung bình pixel.
Cú pháp sử dụng trong OpenCV:
Trong OpenCV, bạn có thể dùng hàm cv2.matchTemplate() để thực hiện template matching:

python
Sao chép mã
cv2.matchTemplate(image, template, method)
image: Ảnh gốc mà bạn muốn tìm kiếm mẫu.
template: Mẫu (template) mà bạn muốn tìm.
method: Phương pháp so khớp (như cv2.TM_CCOEFF, cv2.TM_CCORR, hoặc cv2.TM_SQDIFF).
Kết quả:
Hàm cv2.matchTemplate() trả về một ma trận, trong đó mỗi phần tử đại diện cho mức độ tương tự giữa mẫu và vùng tương ứng trong ảnh gốc. Bạn có thể dùng hàm cv2.minMaxLoc() để tìm vị trí điểm có mức tương đồng cao nhất (hoặc thấp nhất tùy thuộc vào phương pháp).

Ví dụ về Template Matching:
Dưới đây là một ví dụ cơ bản về cách thực hiện template matching trong OpenCV:

python
Sao chép mã
import cv2
import numpy as np

# Đọc ảnh gốc và ảnh mẫu
image = cv2.imread('image.png', 0)
template = cv2.imread('template.png', 0)

# Lấy kích thước mẫu
w, h = template.shape[::-1]

# Thực hiện template matching
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Tìm vị trí tương quan tốt nhất (giá trị maxLoc)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Xác định góc trên bên trái của vùng khớp
top_left = max_loc

# Xác định góc dưới bên phải của vùng khớp
bottom_right = (top_left[0] + w, top_left[1] + h)

# Vẽ hình chữ nhật xung quanh vùng khớp trên ảnh gốc
cv2.rectangle(image, top_left, bottom_right, 255, 2)

# Hiển thị kết quả
cv2.imshow('Template Matching', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
Giải thích:
Đọc ảnh: Đọc ảnh gốc (image.png) và ảnh mẫu (template.png).
Thực hiện template matching: So sánh mẫu với ảnh gốc bằng phương pháp tương quan chuẩn hóa (cv2.TM_CCOEFF_NORMED).
Tìm vị trí tốt nhất: Sử dụng cv2.minMaxLoc() để tìm tọa độ có mức độ tương đồng cao nhất.
Vẽ hình chữ nhật: Dùng tọa độ vừa tìm được để vẽ một hình chữ nhật bao quanh khu vực trùng khớp trên ảnh gốc.
Kết luận:
Template Matching là một phương pháp tìm kiếm một mẫu trong ảnh lớn hơn.
Nó rất hữu ích trong các ứng dụng như phát hiện đối tượng, kiểm tra trực quan, và theo dõi đối tượng.
Tuy nhiên, phương pháp này hoạt động hiệu quả nhất khi kích thước và hướng của mẫu không thay đổi nhiều so với ảnh gốc. Nếu mẫu có sự biến dạng về kích thước, hình dạng hoặc bị che khuất, thì kết quả có thể không chính xác."""

import cv2
import numpy as np


# img = cv2.imread("messi.jpg",0)
# imgf = cv2.imread("messi_face.jpg",0)
# imgO = cv2.imread("messi.jpg")

img = cv2.imread("king2.jpg",0)
imgf = cv2.imread("king3.jpg",0)
imgO = cv2.imread("king3.jpg")

# img = cv2.imread("king.jpg",0)
# imgf = cv2.imread("anhnhom.jpg",0)
# imgO = cv2.imread("anhnhom.jpg")

# img = cv2.imread("king.jpg",0)
# imgf = cv2.imread("anhlop2.jpg",0)
# imgO = cv2.imread("anhlop2.jpg")


h, w = imgf.shape

#So khớp -> mảng trả về là một mảng mức độ khác biệt giữa 2 ảnh
# mangXuLi = cv2.matchTemplate(img, imgf, cv2.TM_SQDIFF_NORMED)
mangXuLi = cv2.matchTemplate(img, imgf, cv2.TM_SQDIFF_NORMED)

# minMaxLoc trả về giá trị nhỏ nhất, lớn nhất, tọa độ nhỏ nhất, tọa độ lớn nhất
_ , _ , minLoc , maxLoc = cv2.minMaxLoc(mangXuLi)

cv2.rectangle(imgO, minLoc, (minLoc[0] + 200, minLoc[1] + 200), (0, 255, 0), 2)



 
cv2.imshow("img", img)
cv2.imshow("img2", imgf)
cv2.imshow("img3", imgO)
cv2.waitKey(0)
cv2.destroyAllWindows()



# video = cv2.VideoCapture(0)
# img = cv2.imread("king2.jpg", 0)




# while True:
#     ret, frame = video.read()
#     frame2 = frame.copy()

#     frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # result = cv2.matchTemplate(frame, img, cv2.TM_CCORR_NORMED)
#     result = cv2.matchTemplate(frame, img, cv2.TM_SQDIFF_NORMED)

#     _ , _ , minLoc , maxLoc = cv2.minMaxLoc(result)

#     cv2.rectangle(frame2, minLoc, (minLoc[0] + 200, minLoc[1] + 200), (0, 255, 0), 2)

#     cv2.imshow("frame", frame2)

#     if cv2.waitKey(1) == ord("q"):
#         break



# video.release()
# cv2.destroyAllWindows()