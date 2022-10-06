from django.contrib import admin
from .models import Article 

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    # class가 많은 이유?
    # 기본 기능을 상속 받아서 커스텀 설정을 하고 이걸 그대로 사용, 나도 사용, Django도 사용
    # 현재는 view를 function으로 정의하고 있지만 view까지도 class로 정의하는 것이 있다.
    # fields = ['title']

admin.site.register(Article, ArticleAdmin)

