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


class Location(models.Model):
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)
    location = models.CharField(default=locat)

    def locat(self):
        return f'{self.address}-{self.zipcode}, {(self.state).capitalize()}, {(self.country).capitalize()}'

    def __str__(self):
        return self.location


class Post(models.Model):
    uploaded_by = models.ForeignKey(User, null=True, related_name='posts')
    name = models.CharField(min_length=200, null=True)
    landing_image = models.ImageField(upload_to='site-images/', null=True)
    screenshot_1 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_2 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_3 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_4 = models.ImageField(upload_to='site-images/', null=True)
    description = models.TextField(blank=True)
    site_link = models.CharField(max_length=200, null=True)
    location = models.ManyToManyField(Location, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    usability = models.FloatField(default=0.00, null=True)
    design = models.FloatField(default=0.00, null=True)
    creativity = models.FloatField(default=0.00, null=True)
    content = models.FloatField(default=0.00, null=True)
    mobile = models.FloatField(default=0.00, null=True)
    is_sotd = models.BooleanField(default=False)
    is_hm = models.BooleanField(default=False)
    is_soty = models.BooleanField(default=False)
    is_mow = models.BooleanField(default=False)
    is_ds = models.BooleanField(default=False)

    @classmethod
    def all_posts(cls):
        all_posts = cls.objects.all()
        return all_posts

    @classmethod
    def user_posts(cls, user_name):
        user = User.objects.filter(username=user_name)[0]
        posts = cls.objects.filter(uploaded_by=user)
        return posts

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(description__icontains=search_term)

    @classmethod
    def get_user_profile(cls, post):
        posts = cls.objects.filter(uploaded_by=post.uploaded_by)
        return posts

    def save_post(self, user):
        self.uploaded_by = user
        self.save()

    def __str__(self):
        return self.name


class Followers(models.Model):
    follower = models.ForeignKey(User, related_name='followers', null=True)
    following = models.ForeignKey(User, related_name='following', null=True)
    followed_on = models.DateTimeField(auto_now_add=True)

    def follow_user(self, current_user, user_other):
        self.following = user_other
        self.follower = current_user
        self.save()

    def unfollow_user(self, user):
        fol = Followers.objects.get(follower=user)
        fol.delete()

    def __str__(self):
        return f'{self.follower.username} is now following {self.following.username}'


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


class PostLikes(models.Model):
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
