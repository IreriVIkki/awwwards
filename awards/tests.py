from django.test import TestCase
from datetime import datetime
# Create your tests here.
from .models import *

#  test categories class


class TestUser (TestCase):
    def setUp(self):
        self.vikki = User(username='vikki', password='akisijui')
        self.vikki.save()

    def tearDown(self):
        User.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.vikki.username, 'vikki')
        self.assertEqual(self.vikki.password, 'akisijui')
        self.assertTrue(isinstance(self.vikki, User))


class TestUserProfile (TestCase):
    def setUp(self):

        self.vikki = User(username='vikki', password='akisijui')
        self.vikki.save()
        self.lord_stark = Profile(user=self.vikki, first_name='Victor',
                                  user_name='Lord_stark', bio='i care', email='vikkicoder@gmail.com')
        self.lord_stark.save_profile(self.vikki)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.lord_stark.first_name, 'Victor')
        self.assertEqual(self.lord_stark.user_name, 'Lord_stark')
        self.assertEqual(self.lord_stark.bio, 'i care')
        self.assertEqual(self.lord_stark.email, 'vikkicoder@gmail.com')
        self.assertTrue(isinstance(self.lord_stark, Profile))

    def test_save_profile(self):
        self.lord_stark.save_profile(self.vikki)
        self.assertTrue(len(Profile.objects.all()) > 0)


class TestPost (TestCase):
    def setUp(self):
        self.vikki = User(username='vikki', password='akisijui')
        self.vikki.save()
        self.waterfall = Post(uploaded_by=self.vikki, landing_image='test.jpg',
                              country='Kenya', post_date=datetime.utcnow())
        self.waterfall.save_post(self.vikki)

    def tearDown(self):
        Post.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.waterfall.uploaded_by, self.vikki)
        self.assertEqual(self.waterfall.landing_image, 'test.jpg')
        self.assertEqual(self.waterfall.country, 'Kenya')
        self.assertTrue(isinstance(self.waterfall, Post))

    def test_all_posts(self):
        self.assertTrue(len(Post.objects.all()) > 0)

    def test_user_posts(self):
        self.assertTrue(len(Post.get_user_profile(self.vikki)) > 0)

class TestComment (TestCase):
    def setUp(self):

        self.vikki = User(username='vikki', password='akisijui')
        self.vikki.save()
        self.waterfall = Photo(uploaded_by=self.vikki, photo='test.jpg',
                               caption='this is a test photo', post_date=datetime.utcnow())
        self.waterfall.save_photo(self.vikki)
        self.comment = Comment(comment='this is comment')
        self.comment.save_comment(self.vikki, self.waterfall)

    def tearDown(self):
        Comment.objects.all().delete()

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_all_photo_comments(self):
        self.assertTrue(len(Comment.all_photo_comments(self.waterfall.id)) > 0)