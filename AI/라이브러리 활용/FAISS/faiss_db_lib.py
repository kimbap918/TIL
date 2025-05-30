############################################################
# 프로그램 : faiss vector db create, query 프로그램
# 개 발 자 : 홍길동
# 작성일자 : 2025.05.21
# 사용방법 : faissFaceCreate ( 사진에서 얼굴이미지만 추출하는 Dataset함수 )
#           faissFaceVectorDB ( Dataset을 벡터DB로 생성하는 함수)
############################################################

# 1. 라이브러리 불러오기
import os
import numpy as np
from PIL import Image
import faiss
import face_recognition

# 2. 환경설정
# 글로벌 변수의 경우 대분자로 사용하는 것이 좋다.
ORG_DATA_PATH       = './data/org_data'  # 원본 데이터 경로
DATASETS_DATA_PATH  = './data/datasets'  # 학습 데이터 경로
VECTOR_DB_PATH      = './vectordb'       # 벡터 DB 경로

############################################################
# 라이브러리
############################################################
# 해당 디렉토리를 모두 확인해서 원본 이미지 파일을 불러오는 함수
def read_file(org_path, createDir):
    # 이미지정보가 저장
    img_path = []
    # 데이터 가져오기
    for paths, subdirs, files in os.walk(org_path):
        print('paths = ', paths)
        print('subdirs = ', subdirs)
        print('files = ', files)
        # exit()

        # 디렉토리에 파일 자동 생성
        if createDir == True:
            createFolder(subdirs)

        for name in files:
            img_path.append(os.path.join(paths, name))

    return img_path

# 디렉토리 자동생성(Dataset 디렉토리를 생성)
def createFolder(dir):
    for data in dir:
        dataset_path = DATASETS_DATA_PATH + '/' + data
        print("Dataset path = ", dataset_path)
        # 만약 디렉토리가 존재하지 않으면 새로 생성
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)

############################################################
# 3. 학습 데이터 전처리 과정
############################################################
def faissFaceCreate():
    ###
    # 원본 이미지의 데이터를 불러오는 함수
    ###
    org_img = read_file(ORG_DATA_PATH, True)
    # print('=' * 50)
    # print('  얼굴만 분리할 원본 데이터 파일 경로  ')
    # print('=' * 50)
    # for data in org_img:
    #     print(data)
    # print('-' * 50)
    ###
    # 불러온 이미지에서 얼굴 추출
    ###
    for path_img in org_img:
        print(path_img)
        # exit()
        # 1. 이미지를 numpy 형태의 숫자 코드로 변환
        img = face_recognition.load_image_file(path_img)
        # print(img)
        # print(img.shape)
        # 2. 얼굴 검출
        img_face = face_recognition.face_locations(img)
        # 얼굴이 1개인 것만 얼굴 전처리
        if len(img_face) != 1:
            continue

        # 얼굴 하나만 검출된 결과
        print(path_img, len(img_face), img_face)

        top, right, bottom, left = img_face[0]
        print('top = ', top)
        print('right = ', right)
        print('bottom = ', bottom)
        print('left = ', left)

        # 마진을 추가해서 추출하는 작업을 해줘야함.
        margin_len = 20
        top     = top - margin_len
        right   = right + margin_len
        bottom  = bottom + margin_len
        left    = left - margin_len

        # numpy slicing 처리
        face_img = img[top:bottom, left:right]
        # 얼굴이 잘 잘라졌는지 확인
        pil_img = Image.fromarray(face_img)
        # pil_img.save('cut_img.jpg')
        # 저장
        dataset_img = path_img.replace('org_data', 'datasets')
        print("dataset_img =", dataset_img)
        try:
            pil_img.save(dataset_img)
        except:
            continue

# dataset에 얼굴만있는 이미지를 vectordb로 생성하는 함수.
def faissFaceVectorDB(dbname):
    dataset_imgs = read_file(DATASETS_DATA_PATH, False)

    # faiss에 얼굴정보를 등록하는 Vectordb에 등록할 리스트
    faceEncode = []
    img_paths = []
    
    for path in dataset_imgs:
        print(path)
        # 얼굴이미지 불러오기
        img = face_recognition.load_image_file(path)

        try:
            face_encode = face_recognition.face_encodings(img)[0]
        except:
            continue

        print(face_encode)
        print(len(face_encode))

        # 배열에 저장
        faceEncode.append(face_encode)
        face_name = path.split('\\')[-2]
        print("face_name = ", face_name)
        img_paths.append(face_name)
    
    print("검출된 얼굴은 총 {}개입니다.".format(len(faceEncode)))
    train_labels = np.array(img_paths)
    print(train_labels)

    # 벡터 DB를 만드려면
    print("faceEncode :", type(faceEncode))
    print("train_lables :", type(train_labels))

    # 인코딩을 위한 변환작업( faceEncode는 Numpy )
    faceEncode = np.array(faceEncode, dtype=np.float32)
    print(faceEncode.shape, train_labels.shape)

    # 벡터DB를 생성
    face_index = faiss.IndexFlatL2(128)
    # 벡터DB에 데이터 저장
    face_index.add(faceEncode)
    # 벡터DB저장
    faiss.write_index(
        face_index,
        VECTOR_DB_PATH + '/' + dbname + '.bin'
    )
    # 넘파이 정답
    np.save(
        VECTOR_DB_PATH + '/' + dbname + '.npy',
        train_labels
        )

############################################################
# 테스트...
############################################################
# faissFaceCreate()
faissFaceVectorDB('face_20250521')