from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

def index(request):
	return render(request, 'base.html')

class IndexView(ListView):
	pass
	# model = Post
	# template_name = 'base.html'
	# context_object_name = 'post_list'
	# paginate_by = 10
