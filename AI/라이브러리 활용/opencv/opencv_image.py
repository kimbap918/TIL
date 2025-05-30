import cv2

# 이미지 불러오기
image = cv2.imread('./aespa.jpg', cv2.IMREAD_COLOR)
print("image type = ", type(image))
# 그레이(흑백) 이미지로 표시
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 흑백 이미지 특정 부분 자르기
cut_image = gray_image[100:500, 200:700].copy()

# 원본 이미지 표시
cv2.imshow('aespa image', image)
cv2.imshow('aespa gray image', gray_image)
cv2.imshow('aespa cut image', cut_image)

cv2.imwrite('./aespa_gray.jpg', gray_image)
cv2.imwrite('./aespa_cut.jpg', cut_image)

# 키를 누를때 까지 기다림
cv2.waitKey(0)

# 종료할때
cv2.destroyAllWindows()