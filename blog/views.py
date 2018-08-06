from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

def index(request):
	return HttpResponse("Hello World")

class IndexView(ListView):
	model = Post
	template_name = 'base.html'
	context_object_name = 'post_list'
	paginate_by = 10
