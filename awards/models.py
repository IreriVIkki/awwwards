from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile')
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='images/', blank=True,)
    user_name = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=300, null=True)
    bio = models.TextField(blank=True)
    website = models.CharField(max_length=150, null=True)
    facebook = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    STATUS_CHOICES = (
        ('Male', ("Male")),
        ('Female', ("Female")),
        ('Other', ("Other")),
    )
    gender = models.CharField(
        max_length=20, choices=STATUS_CHOICES, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=150, null=True)
    is_judge = models.BooleanField(default=False)
    is_pro = models.BooleanField(default=False)
    is_chief = models.BooleanField(default=False)
    is_tribe = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'userprofile'


class Post(models.Model):
    pass


class tags(models.Model):
    pass


class technologies(models.Model):
    pass


class Rating(models.Model):
    pass


class Comment(models.Model):
    pass


class Collection(models.Model):
    pass


class PhotoLikes(models.Model):
    pass


class CommentsLikes(models.Model):
    pass


class SiteOfDay(models.Model):
    pass


class SiteOfYear(models.Model):
    pass


class HonorableMention(models.Model):
    pass


class MobileOfWeek(models.Model):
    pass


class DeveloperSite(models.Model):
    pass
