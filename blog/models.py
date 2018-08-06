import markdown

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html	import strip_tags


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
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-created_time']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={ 'pk': self.pk })

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])
	
	def save(self, *args, **kwargs):
		if not self.excerpt:
			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
			])
			self.excerpt = strip_tags(md.convert(self.body))[:54]	
		super(Post, self).save(*args, **kwargs)