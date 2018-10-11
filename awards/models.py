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
    uploaded_by = models.ForeignKey(User, null=True, related_name='posts')
    name = models.CharField(max_length=200, null=True)
    landing_image = models.ImageField(upload_to='site-images/', null=True)
    screenshot_1 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_2 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_3 = models.ImageField(upload_to='site-images/', null=True)
    screenshot_4 = models.ImageField(upload_to='site-images/', null=True)
    description = models.TextField(blank=True)
    site_link = models.CharField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
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
    def user_posts(cls, user_id):
        user = User.objects.get(pk=user_id)
        posts = user.posts.all()
        return posts

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(description__icontains=search_term)

    @classmethod
    def get_user_profile(cls, post):
        posts = cls.objects.filter(uploaded_by=post.uploaded_by)
        return posts

    @classmethod
    def get_one_post(cls, post_id):
        return cls.objects.get(pk=post_id)

    def save_post(self, user):
        self.uploaded_by = user
        self.save()

    def __str__(self):
        return self.name


class Location(models.Model):
    post = models.ForeignKey(Post, null=True, related_name='location')
    user = models.ForeignKey(User, null=True, related_name='address')
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)

    @classmethod
    def locat(cls):
        return f'{cls.address}-{cls.zipcode}, {cls.state}, {cls.country}'
    location = models.CharField(max_length=500, default=locat)

    def __str__(self):
        return self.location


class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', null=True)
    post = models.ForeignKey(Post, related_name='ratings', null=True)
    usability = models.FloatField(default=0.00, null=True)
    design = models.FloatField(default=0.00, null=True)
    creativity = models.FloatField(default=0.00, null=True)
    content = models.FloatField(default=0.00, null=True)
    mobile = models.FloatField(default=0.00, null=True)

    @property
    def average_judge_rating(self, null=True):
        rated = [i for i in [self.usability, self.design,
                             self.creativity, self.content, self.mobile] if i != None]
        rating = sum(rated[0:len(rated)])/len(rated)
        print(rating)
        return rating

    @classmethod
    def average_usability(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.usability for ur in post_ratings]
        average = sum(_all)/len(_all)
        print(average)
        return average

    @classmethod
    def average_design(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.design for ur in post_ratings]
        average = sum(_all)/len(_all)
        print(average)
        return average

    @classmethod
    def average_creativity(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.creativity for ur in post_ratings]
        average = sum(_all)/len(_all)
        print(average)
        return average

    @classmethod
    def average_content(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.content for ur in post_ratings]
        average = sum(_all)/len(_all)
        print(average)
        return average

    @classmethod
    def average_mobile(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.mobile for ur in post_ratings]
        average = sum(_all)/len(_all)
        print(average)
        return average

    @classmethod
    def average_rating(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.average_judge_rating for ur in post_ratings]
        average = sum(_all)/len(_all)
        print(average)
        return average

    @classmethod
    def get_last_post(cls):
        return cls.objects.last()


class Followers(models.Model):
    follower = models.ForeignKey(User, related_name='followers', null=True)
    following = models.ForeignKey(User, related_name='following', null=True)
    followed_on = models.DateTimeField(auto_now_add=True)

    def follow_user(self, current_user, user_other):
        self.following = user_other
        self.follower = current_user
        self.save()

    @classmethod
    def unfollow_user(cls, user):
        fol = cls.objects.get(follower=user)
        fol.delete()

    def __str__(self):
        return f'{self.follower.username} is now following {self.following.username}'


class tags(models.Model):
    post = models.ForeignKey(Post, related_name='tags', null=True)
    tag = models.CharField(max_length=50, null=True)


class technologies(models.Model):
    post = models.ForeignKey(Post, related_name='technologies', null=True)
    tag = models.CharField(max_length=50, null=True)


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', null=True)
    post = models.ForeignKey(Post, related_name='comments', null=True)
    rating = models.TextField(null=True)


class Collection(models.Model):
    user = models.ForeignKey(User, related_name='collections', null=True)
    post = models.ForeignKey(Post)


class PostLikes(models.Model):
    user = models.ForeignKey(User, related_name='liked_posts', null=True)
    post = models.ForeignKey(Post, related_name='likes', null=True)


class CommentsLikes(models.Model):
    user = models.ForeignKey(User, related_name='liked_by', null=True)
    comment = models.ForeignKey(Comment, related_name='likes', null=True)
