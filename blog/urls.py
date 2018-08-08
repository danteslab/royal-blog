from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('post/<int:pk>/', views.DetailView.as_view(), name="detail")
]