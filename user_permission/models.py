# models.py
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_publish", "Can publish posts")
        ]


def create_custom_permission():
    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.create(
        codename="can_publish",
        name="Can publish posts",
        content_type=content_type
    )
