from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.db import models
from django.conf import settings

# Create your models here.
'''
게시판 기능 
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
'''
# 1. 모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(400, 300)],
                                format='JPEG',
                                options={'quality': 80})
    image_thumbnail = ProcessedImageField(
	                                      upload_to = 'images/', 	blank=True,# settings.py 원본 ImageField 명
	                                      processors = [Thumbnail(100, 100)], # 처리할 작업목록
		                                  format = 'JPEG',		   # 최종 저장 포맷
		                                  options = {'quality': 60}) # 저장 옵션
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # user는 settings.AUTH_USER_MODEL에 정의된 accounts앱에 user 클래스
    # 역참조해서 사용 : user.comment_set.all()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, null=True)