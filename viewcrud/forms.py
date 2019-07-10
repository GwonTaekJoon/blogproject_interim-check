from django import forms
from .models import Blog, Comment

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        #fields = '__all__' -> 모든 항목을 입력받겠다.
        fields = ['title','body']  #fields라는 리스트에 title과 body항목만 입력 받겠다.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)