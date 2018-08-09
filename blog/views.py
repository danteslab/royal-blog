import markdown

from markdown.extensions.toc import TocExtension

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.utils.text import slugify

from .models import Post, Category, Tag

class IndexView(ListView):
	model = Post
	template_name = 'blog/index.html'
	context_object_name = 'post_list'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		paginator = context.get('paginator')
		page = context.get('page_obj')
		is_paginated = context.get('is_paginated')
		pagination_data = self.pagination_data(paginator, page, is_paginated)
		context.update(pagination_data)
		return context

	def pagination_data(self, paginator, page, is_paginated):
		if not is_paginated:
			return {}

		left = []

		rigth = []
		left_has_more = False
		rigth_has_more = False
		first = False
		last = False

		page_number = page.number
		total_pages = paginator.page_range

		if page_number == 1:
			rigth = page_range[page_number:page_number + 2]

			if rigth[-1] < total_pages - 1:
				rigth_has_more = True

			if rigth[-1] < total_pages:
				last = True
		elif page_number == total_pages:
			left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

			if left[0] > 2:
				left_has_more = True

			if left[0] > 1:
				first = True
		else:
			left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
			rigth = page_range[page_number:page_number + 2]

			if rigth[-1] < total_pages - 1:
				rigth_has_more = True
			if rigth[-1] < total_pages:
				last = True

			if left[0] > 2:
				left_has_more = True
			if left[0] > 1:
				first = True
		data = {
			'left': left,
			'right': rigth,
			'left_has_more': left_has_more,
			'rigth_has_more': rigth_has_more,
			'first': first,
			'last': last,
		}

		return data

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail.html'
	context_object_name = 'post'

	def get(self, request, *args, **kwargs):
		response = super(PostDetailView, self).get(request, *args, **kwargs)

		self.object.increase_views()

		return response

	def get_object(self, queryset=None):
		post = super(PostDetailView, self).get_object(queryset=None)
		md = markdown.Markdown(extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			TocExtension(slugify=slugify),
		])
		post.body = md.convert(post.body)
		post.toc = md.toc
		return post

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		# form = CommentForm()
		# comment_list = 
		context.update({
			'form': None,
			'comment_list': None,

			})
		return context

