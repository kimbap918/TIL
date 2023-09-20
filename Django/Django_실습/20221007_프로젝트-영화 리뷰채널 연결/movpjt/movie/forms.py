from django import forms
from .models import Review

 
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # 제목, 내용, 이름, 평점을 사용자에게 입력받음 + 유효성 검사
        fields = ['title', 'content', 'movie_name', 'grade']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 100px;'}),
            'movie_name' : forms.TextInput(attrs={'class':'form-control'}),
            'grade' : forms.TextInput(attrs={'class':'form-control'}),
        }
