# 애플리케이션 폴더에 forms.py 생성하기
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "summary", "running_time"]
