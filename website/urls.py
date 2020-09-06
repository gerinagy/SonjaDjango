from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('contact.html', views.contact, name="contact"),
	path('blog.html', views.blog, name="blog"),
	path('about.html', views.about, name="about"),
]
