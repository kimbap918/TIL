############################################################
# 프로그램 : faiss vector db create, query 프로그램
# 개 발 자 : 홍길동
# 작성일자 : 2025.05.21
# 사용방법 : faissFaceLoad ( faiss 정보를 불러온다 )
#           faissFaceSearch ( faiss 에서 정보를 검색한다. )
############################################################

# 1. 라이브러리 불러오기
import os
import numpy as np
from PIL import Image
import faiss
import face_recognition

# 글로벌 변수로 지정
FAISS_INDEX     = ''   # 학습된 벡터 DB파일
FAISS_LABEL     = ''   # 학습된 벡터 결과파일
VECTOR_DB_PATH  = './vectordb'       # 벡터 DB 경로

# 2. 학습된 faiss 라이브러리의 정보 불러오기
def faissFaceLoad(loadFile):
    global FAISS_INDEX, FAISS_LABEL

    try:
        FAISS_INDEX = faiss.read_index(VECTOR_DB_PATH + '/' + loadFile + '.bin')
        FAISS_LABEL = np.load(VECTOR_DB_PATH + '/' + loadFile + '.npy')
    except:
        print("FAISS 데이터베이스를 불러오는데 실패하였습니다.")
        exit()

# 이미지를 검색
def faissFaceSearch(img):
    global FAISS_INDEX, FAISS_LABEL

    # 얼굴 검출
    test_img = face_recognition.load_image_file(img)
    test_face = face_recognition.face_locations(test_img)
    if len(test_face) != 1:
        print("얼굴을 찾기 못하였습니다.")
        exit()
    
    top, right, bottom, left = test_face[0]
    # 마진을 추가해서 추출하는 작업을 해줘야함.
    margin_len = 20
    top     = top - margin_len
    right   = right + margin_len
    bottom  = bottom + margin_len
    left    = left - margin_len

    # numpy slicing 처리
    face_img = test_img[top:bottom, left:right]
    # 얼굴이 잘 잘라졌는지 확인
    pil_img = Image.fromarray(face_img)
    pil_img.save('./source/temp.jpg')

    img = face_recognition.load_image_file('./source/temp.jpg')

    # 인코딩
    test_en = face_recognition.face_encodings(img)[0]
    print(test_en.shape)
    test_en = np.array(test_en, dtype=np.float32).reshape(-1, 128)
    print(test_en.shape)

    # 예측
    distance, result = FAISS_INDEX.search(test_en, k=5)
    print('distance = ', distance)
    print('result = ', result)

    # 답을 확인
    for i in result:
        print(FAISS_LABEL[i])

########################################################
# 실행
########################################################
# 불러오기
faissFaceLoad('face_20250521')
faissFaceSearch('./source/test4.jpg')
