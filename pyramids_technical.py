"""
Kỹ thuật Pyramid trong OpenCV là một phương pháp xử lý ảnh nhằm thay đổi độ phân giải của ảnh theo các mức khác nhau. Nó giúp ích trong nhiều ứng dụng như phát hiện vật thể, theo dõi chuyển động, và xử lý hình ảnh với các kích thước khác nhau. Có hai loại pyramid chính:

Gaussian Pyramid: Giảm độ phân giải của ảnh bằng cách áp dụng bộ lọc Gaussian và sau đó giảm kích thước ảnh. Kỹ thuật này thường được sử dụng để giảm chi tiết không cần thiết hoặc chuẩn bị cho các thuật toán phân tích đa độ phân giải.

Laplacian Pyramid: Là sự kết hợp giữa Gaussian Pyramid và ảnh gốc để tạo ra ảnh có độ chi tiết cao hơn. Nó được sử dụng trong các ứng dụng như nén ảnh, trộn ảnh (image blending), và tái tạo ảnh từ các mức độ phân giải khác nhau.

Ứng dụng thực tế của kỹ thuật Pyramid:
Phát hiện vật thể (Object Detection): Khi kích thước của vật thể thay đổi trong ảnh, pyramid cho phép phân tích vật thể ở các mức độ khác nhau, giúp cải thiện khả năng phát hiện.
Theo dõi chuyển động (Motion Tracking): Sử dụng pyramid để tính toán các vector chuyển động ở các mức độ phân giải khác nhau, giúp theo dõi chuyển động chính xác hơn trong trường hợp có nhiều nhiễu.
Nén ảnh: Laplacian pyramid có thể được sử dụng để mã hóa và nén ảnh hiệu quả, giữ lại các chi tiết quan trọng.
Xử lý đa độ phân giải (Multi-resolution Processing): Ứng dụng trong các kỹ thuật như tạo ảnh toàn cảnh (panorama stitching) hay trộn ảnh (image blending).
Nhờ pyramid, các thuật toán có thể hoạt động trên ảnh với nhiều độ phân giải, từ đó tăng hiệu suất và độ chính xác khi xử lý ảnh trong các trường hợp phức tạp.
"""


import numpy as np
import cv2



img = cv2.imread('lena-1.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)



# layer = gp[5]
# cv2.imshow("uupper level Gaussian Pyramids", layer)
# lp = [layer]

# for i in range(5, 0, -1):
#     gaussian_extend = cv2.pyrUp(gp[i])     
#     laplacian = cv2.subtract(gp[i-1], gaussian_extend)
#     cv2.imshow(str(i), laplacian)

# cv2.imshow("origin image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()