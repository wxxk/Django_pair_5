from dataclasses import fields
from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ("user", "like_users")
        labels = {
            'title': '글 제목',
            'content': '글 내용',
            'movie_name': '영화 제목',
            'grade': '평점',
            'image': '이미지 파일'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            'content': '댓글',
        }