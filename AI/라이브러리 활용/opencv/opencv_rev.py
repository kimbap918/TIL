import cv2

# 이미지 불러오기
image = cv2.imread('./aespa.jpg', cv2.IMREAD_COLOR)

# 대칭
rev_image = cv2.flip(image, 1)

# 원본 이미지 표시
cv2.imshow('aespa image', image)
cv2.imshow('aespa rev', rev_image)

# 키를 누를때 까지 기다림
cv2.waitKey(0)
# 종료할때
cv2.destroyAllWindows()