from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="member_index"),
    #################################################################
    # 관리자 로그인(auth)
    #################################################################
    path("login/", views.login, name="login"),
    path("login/auth/", views.login_auth, name="login_auth"),
    path("logout/", views.logout, name="logout"),

    #################################################################
    # 회원관리 URL
    #################################################################
    # 회원 리스트 : Read
    path("", views.member_list, name="member_list"),
    # 회원데이터 추가 / 저장 (Create)
    path("add/", views.member_add, name="member_add"),
    path("add/save/", views.member_add_save, name="member_add_save"),
    # 회원데이터 삭제 (Delete)
    path("delete/<int:id>/", views.member_delete, name="member_delete"),
    # 회원데이터 수정 (Update)
    path("update/<int:idx>/", views.member_update, name="member_update"),
    path("update/save/", views.member_update_save, name="member_update_save"),

    #################################################################
    # 카메라제어
    #################################################################

]