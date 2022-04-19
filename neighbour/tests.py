from django.test import TestCase
from .models import UserProfile, Neighbourhood, Post, Business
from django.contrib.auth.models import User
# Create your tests here.
class TestNeighbourhood(TestCase):
    def setUp(self):
        self.user = User(userprofile='admin')
        self.user.save()

        self.nei = Neighbourhood(image='images',neighbourhood_name='test_neighbour',location='nairobi', occupants=3, admin=self.user  )
        self.nei.save_neighbours()

    def test_instance(self):
        self.assertTrue(isinstance(self.nei,Neighbourhood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_delete_image(self):
        self.nei.delete_neighbourhood()
        image = Neighbourhood.objects.all()
        self.assertEqual(len(image), 0)


class TestBusiness(TestCase):
    def setUp(self):
        self.user = User(userprofile='admin')
        self.user.save()

        self.nei = Neighbourhood(image='images',neighbourhood_name='test_neighbour',location='nairobi', occupants=3, admin=self.user  )
        self.nei.save()

        self.business= Business(name='Business',description='Business description', user=self.user, neighbourhood_name=self.nei, email='business@gmail.com')
        self.business.save_business()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def tearDown(self):
        Business.objects.all().delete()

    def test_delete_image(self):
        self.business.delete_business()
        image = Business.objects.all()
        self.assertEqual(len(image), 0)


class TestPost(TestCase):
    def setUp(self):
        self.user = User(userprofile='admin')
        self.user.save()

        self.post= Post(title='Business', image='images.jpg',description='Business description', posted_by=self.user)
        self.post.save_post()


    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def tearDown(self):
        Post.objects.all().delete()

    def test_delete_post(self):
        self.post.delete_post()
        image = Post.objects.all()
        self.assertEqual(len(image), 0)


class TestUserProfile(TestCase):
    def setUp(self):
        self.user = User(userprofile='admin')
        self.user.save()

        self.nei = Neighbourhood(image='images',neighbourhood_name='test_neighbour',location='nairobi', occupants=3, admin=self.user  )
        self.nei.save_neighbours()

        self.profile= UserProfile(name='John',national_identity_no=11111,  neighbourhood_name=self.nei, email='john@gmail.com', user=self.user, profile_picture='image.jpg', bio="Amazing person")
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,UserProfile))

    def tearDown(self):
        UserProfile.objects.all().delete()

    def test_delete_image(self):
        self.profile.delete_profile()
        image = UserProfile.objects.all()
        self.assertEqual(len(image), 1)


