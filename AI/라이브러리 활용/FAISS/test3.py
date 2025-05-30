import os
import numpy as np
from PIL import Image
import faiss
import face_recognition

path_img = './data/org_data/008_chuu/4.jpg'

try:
    img = face_recognition.load_image_file(path_img)
    img_face = face_recognition.face_locations(img)
    top, right, bottom, left = img_face[0]
    face_img = img[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.save('./testimg.jpg')
except:
    print("에러네...")