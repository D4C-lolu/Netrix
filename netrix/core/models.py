from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES = (
    ("Family", "Family"),
    ("Kids", "Kids"),
    ("Teens", "Teens"),
    ("Mature", "Mature"),
)

MOVIE_CHOICES = (("seasonal", "seasonal"), ("single", "single"))


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank=True)


class Profile(models.Model):

    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):

    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    genre = models.CharField(max_length=30, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField("Video")
    thumbnail = models.ImageField(upload_to="thumbnails")
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)


class Video(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to="movies")
