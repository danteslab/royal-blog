from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200, blank=True)
	# View cunter in publications.
	views = models.PositiveIntegerField(default=0)
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User)

	class Meta:
		ordering = ['-created_time']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={ 'pk': self.pk })

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])