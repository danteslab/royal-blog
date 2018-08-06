import datetime

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post, Tag, Category

class PostModelTests(TestCase):
	def test_was_created_correctly(self):
		time = timezone.now()
		user = User(username='tesla', email='tesla@gmail.com', password='teslaispower')
		user.save()
		django_cat = Category(name='django')
		django_cat.save()
		programming_tag = Tag(name='programming')
		web_development_tag = Tag(name='web development')

		post = Post(
			title='My First Post',
			body='Hi, this is my first post and I\'ll show you how to create a blog with Django.',
			created_time=time,
			modified_time=time,
			excerpt='Hi, this is my first post.',
			category=django_cat,			
			author=user
			)
		post.save() # Here is the test.
		self.assertEquals(str(post), 'My First Post')