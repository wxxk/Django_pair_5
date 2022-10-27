from dataclasses import fields
from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ("user", "like_users")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
