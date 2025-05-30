from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("LANDING 페이지 입니다.")
    #  데이터 구조 만들기
    sendData = {
        "titles" : "인공지능 출입관리 프로젝트 V1.0",
        "sub_titles" : "Face Recognition, Dlib, CNN, FAISS, OpenCV등 기술적용",
        "state_msg" : "서비스 시작",
    }
    
    return render(request, "landing/main.html", sendData)