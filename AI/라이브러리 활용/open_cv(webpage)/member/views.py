from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth, User

from api.models import Members

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def index(request):
    return HttpResponse("MEMBER 페이지 입니다.")

def login(request):
    return render(request, "auth/login.html")

def logout(request):
    # 로그아웃 처리
    auth.logout(request)
    # 로그아웃 후 이동할 페이지
    return redirect("login")

def login_auth(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")
    
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")

    print("email :", email)
    print("password :", password)

    # email을 이용해서 username을 가져온다.
    username = User.objects.get(email=email)

    # 로그인 인증
    user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        # 로그인 성공
        return redirect("member_list")
    else:
        # 로그인 실패
        return HttpResponse("로그인 인증 실패")

    return HttpResponse("로그인 인증 처리")

@login_required(login_url="/member/login/")
def member_update_save(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")
    
    # 받야야할 데이터
    # id, password, email, phone
    id = request.POST.get("id", "")
    old_password = request.POST.get("old_password", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")

    print("id :", id)
    print("password :", old_password)
    print("email :", email)
    print("phone :", phone)

    # 데이터를 수정하려면 id값이 일치하는 것만 수정
    try:
        memEdit = Members.objects.get(id=id, password=old_password)
    except:
        return HttpResponse("암호가 일치하지 않습니다.")

    # 수정
    memEdit.email = email
    memEdit.phone = phone
    memEdit.save()

    # 데이터 받아오기
    return redirect("member_list")

@login_required(login_url="/member/login/")
def member_update(request, idx):
    print("idx :", idx)

    # idx에 맞는 회원 정보를 가져온다.
    # (SQL) SELECT * FROM api_members WHERE id = idx
    try:
        memData = Members.objects.get(id=idx)
    except:
        # 에러처리
        return HttpResponse("회원정보가 존재하지 않습니다.")
    
    # print("SQL : ", memData.query)
    # 가져온 값 확인
    print("id :", memData.id)
    print("ids :", memData.ids)
    print("usernames :", memData.usernames)
    print("password :", memData.password)
    print("email :", memData.email)
    print("phone :", memData.phone)

    return render(request, "member/member_update.html", {"data":memData})

@login_required(login_url="/member/login/")
def member_delete(request, id):
    # 회원삭제
    # (SQL) DELETE FROM api_members WHERE id = 1
    # DELETE FROM `api_members` WHERE `id` = 1
    # 장고에서 데이터를 삭제할때 테이블명.objects.filter(조건).delete()
    # 테이블명.objects.filter(조건).delete() <= 조건에 맞는 데이터 삭제
    # 테이블명.objects.get(조건).delete() <= 조건에 맞는 데이터 1건 삭제
    Members.objects.filter(id=id).delete()

    return redirect("member_list")

@login_required(login_url="/member/login/")
def member_list(request):
    # 회원데이터 불러오기(역순)
    # (SQL) SELECT * FROM api_members ORDER BY id DESC
    # SELECT * FROM `api_members` ORDER BY `id` DESC
    # 장고에서 데이터를 호출할때 테이블명.objects.all()
    # 테이블명.objects.all() <= 모든 데이터 호출
    # 테이블명.objects.all().order_by("-id") <= 역순으로 정렬
    memList = Members.objects.all().order_by("-id")
    print("SQL : ", memList.query)

    # 데이터 확인
    for mem in memList:
        print("id :", mem.id)
        print("ids :", mem.ids)
        print("usernames :", mem.usernames)
        print("password :", mem.password)
        print("email :", mem.email)
        print("phone :", mem.phone)
        print("cnts :", mem.cnts)
        print("first_dates :", mem.first_dates)
        print("first_ips :", mem.first_ips)

    return render(request, "member/member_list.html", {"data": memList})

@login_required(login_url="/member/login/")
def member_add(request):
    return render(request, "member/member_add.html")

@login_required(login_url="/member/login/")
def member_add_save(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")

    # 입력된 데이터 저장
    ids = request.POST.get("ids", "")
    usernames = request.POST.get("usernames", "")
    password = request.POST.get("password", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")

    print("ids :", ids)
    print("usernames :", usernames)
    print("password :", password)
    print("email :", email)
    print("phone :", phone)

    # 회원등록
    saveMember = Members()
    saveMember.ids = ids
    saveMember.usernames = usernames
    saveMember.password = password
    saveMember.email = email
    saveMember.phone = phone
    saveMember.cnts = 0
    saveMember.first_dates = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    saveMember.first_ips = get_client_ip(request)
    saveMember.save()

    return redirect("member_list")