from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from django.conf import settings


# Create your models here.
class Review(models.Model):
    star_grade = (
        ("1", "🤩"),
        ("2", "🤩🤩"),
        ("3", "🤩🤩🤩"),
        ("4", "🤩🤩🤩🤩"),
        ("5", "🤩🤩🤩🤩🤩"),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    movie_name = models.CharField(max_length=100)
    grade = models.CharField(max_length=1, choices=star_grade)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )


class Comment(models.Model):
    content = models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
