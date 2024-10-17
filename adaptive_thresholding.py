"""
### **Ngưỡng Thích Ứng (Adaptive Thresholding)**

Ngưỡng thích ứng là một kỹ thuật **phân ngưỡng** trong xử lý ảnh mà ngưỡng được tính toán dựa trên **mỗi vùng nhỏ của hình ảnh** thay vì sử dụng một giá trị ngưỡng cố định cho toàn bộ ảnh (như trong phân ngưỡng toàn cục).

Ngưỡng thích ứng đặc biệt hữu ích khi hình ảnh có **độ chiếu sáng không đồng đều** hoặc các vùng sáng tối khác nhau. Trong những trường hợp này, việc sử dụng một ngưỡng cố định có thể không hiệu quả vì một số vùng có thể quá sáng hoặc quá tối so với các vùng khác.

### **Nguyên Tắc Hoạt Động**
Thay vì sử dụng một giá trị ngưỡng duy nhất, ngưỡng thích ứng tính toán giá trị ngưỡng riêng cho **mỗi pixel** dựa trên các pixel xung quanh nó (trong một vùng nhỏ xung quanh).

Cụ thể, OpenCV hỗ trợ hai phương pháp tính ngưỡng thích ứng:

1. **Adaptive Mean Thresholding**: Giá trị ngưỡng tại mỗi pixel được tính bằng giá trị trung bình của các pixel lân cận trong vùng nhỏ xung quanh trừ đi một hằng số (`C`).

2. **Adaptive Gaussian Thresholding**: Giá trị ngưỡng tại mỗi pixel được tính bằng tổng trọng số của các pixel lân cận, với trọng số được tính dựa trên hàm phân phối Gaussian (phân phối chuẩn) trừ đi một hằng số (`C`).

### **Cú Pháp trong OpenCV**
```python
cv2.adaptiveThreshold(src, maxval, adaptiveMethod, thresholdType, blockSize, C)
```

### **Các Tham Số**
- **`src`**: Ảnh đầu vào (ảnh xám, grayscale).
  
- **`maxval`**: Giá trị tối đa được gán cho các pixel thỏa mãn điều kiện ngưỡng. Thường là 255.

- **`adaptiveMethod`**: Phương pháp tính giá trị ngưỡng.
  - **`cv2.ADAPTIVE_THRESH_MEAN_C`**: Sử dụng giá trị trung bình của các pixel lân cận.
  - **`cv2.ADAPTIVE_THRESH_GAUSSIAN_C`**: Sử dụng tổng trọng số của các pixel lân cận, với trọng số dựa trên phân phối Gaussian.

- **`thresholdType`**: Loại phân ngưỡng.
  - **`cv2.THRESH_BINARY`**: Pixel có giá trị lớn hơn ngưỡng sẽ được gán giá trị `maxval`, pixel nhỏ hơn ngưỡng sẽ được gán giá trị 0.
  - **`cv2.THRESH_BINARY_INV`**: Pixel có giá trị lớn hơn ngưỡng sẽ được gán giá trị 0, pixel nhỏ hơn ngưỡng sẽ được gán giá trị `maxval`.

- **`blockSize`**: Kích thước của vùng lân cận (kích thước của khối) dùng để tính giá trị ngưỡng cho mỗi pixel. Đây phải là số lẻ, ví dụ: 3, 5, 7, v.v.

- **`C`**: Một hằng số được trừ vào giá trị trung bình hoặc giá trị trọng số. Điều này cho phép bạn tinh chỉnh ngưỡng, giúp tăng hoặc giảm giá trị ngưỡng tại mỗi vùng.

### **Ví Dụ Cụ Thể**

Dưới đây là một ví dụ sử dụng ngưỡng thích ứng để xử lý ảnh:

```python
import cv2

# Đọc ảnh gốc dưới dạng grayscale
img = cv2.imread('noisy_image.png', 0)

# Áp dụng Adaptive Mean Thresholding
adaptive_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 11, 2)

# Áp dụng Adaptive Gaussian Thresholding
adaptive_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)

# Hiển thị ảnh gốc và các ảnh sau khi áp dụng ngưỡng thích ứng
cv2.imshow('Original', img)
cv2.imshow('Adaptive Mean Thresholding', adaptive_mean)
cv2.imshow('Adaptive Gaussian Thresholding', adaptive_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

### **Các Tham Số Chính Trong Ví Dụ Trên:**
1. **`img`**: Ảnh đầu vào, trong trường hợp này là ảnh xám.
2. **`255`**: Đây là giá trị tối đa (maxval), tức là các pixel vượt qua ngưỡng sẽ được gán giá trị 255 (màu trắng).
3. **`cv2.ADAPTIVE_THRESH_MEAN_C`**: Sử dụng phương pháp Adaptive Mean để tính giá trị ngưỡng.
4. **`cv2.THRESH_BINARY`**: Sử dụng phân ngưỡng nhị phân, tức là các pixel vượt qua ngưỡng sẽ được gán giá trị `255`, các pixel khác sẽ được gán giá trị `0`.
5. **`11`**: Kích thước của vùng lân cận (block size). Kích thước này phải là số lẻ.
6. **`2`**: Hằng số `C` được trừ vào giá trị ngưỡng để tinh chỉnh.

### **Khi Nào Sử Dụng Adaptive Thresholding?**
- **Khi hình ảnh có độ chiếu sáng không đồng đều**: Ví dụ, ảnh có nhiều vùng sáng và tối khác nhau. Sử dụng một ngưỡng cố định có thể không hoạt động tốt vì những vùng tối có thể bị mất thông tin hoặc bị bỏ qua. Adaptive thresholding xử lý tốt hơn trong các trường hợp này.
  
- **Khi cần phân đoạn đối tượng trong ảnh**: Nếu các đối tượng bạn muốn tách ra khỏi nền có sự thay đổi về ánh sáng trong các phần khác nhau của hình ảnh, adaptive thresholding sẽ giúp phân tách các đối tượng này rõ ràng hơn.

### **Minh Họa Trực Quan**
Giả sử bạn có một bức ảnh của một tài liệu giấy, nhưng ánh sáng không đều trên bề mặt của nó — một phần ảnh bị sáng quá mức, một phần bị tối đi. Phân ngưỡng cố định có thể chỉ hiệu quả ở một số vùng, trong khi adaptive thresholding sẽ điều chỉnh ngưỡng tại mỗi vùng riêng biệt, cho phép bạn phân tách văn bản từ nền giấy một cách hiệu quả.

### **Kết Luận**
Ngưỡng thích ứng là một công cụ mạnh mẽ để xử lý các hình ảnh có độ chiếu sáng không đồng đều. Nó giúp tự động tính toán ngưỡng cho từng vùng nhỏ trong ảnh, từ đó làm nổi bật đối tượng cần quan tâm. Trong OpenCV, `cv2.adaptiveThreshold()` cung cấp hai phương pháp tính ngưỡng thích ứng là phương pháp Mean và Gaussian, cho phép người dùng tùy chọn và tinh chỉnh ngưỡng theo nhu cầu cụ thể của bài toán.

"""


import cv2 



#nhan anh voi loai xam
img = cv2.imread("cancuoc.jpg",0)
cv2.imshow("img", img)

#xu li voi global thresholding
_ ,img2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("img2", img2)

#xu li voi adaptive thresholding
img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("img3",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


