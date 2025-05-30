from django.db import models

# Create your models here.
class Members(models.Model):
    ids         = models.CharField(max_length=100, null=False, verbose_name='아이디')
    usernames   = models.CharField(max_length=100, null=False, verbose_name='이름')
    password    = models.CharField(max_length=100, null=False, verbose_name='비밀번호')
    email       = models.CharField(max_length=100, null=False, verbose_name='이메일')
    phone       = models.CharField(max_length=100, null=False, verbose_name='전화번호')
    cnts        = models.IntegerField(default=0, verbose_name='방문수')
    first_dates = models.CharField(max_length=20, null=False, verbose_name='가입일')
    first_ips   = models.CharField(max_length=20, null=False, verbose_name='가입IP')

    def __str__(self):
        return self.usernames