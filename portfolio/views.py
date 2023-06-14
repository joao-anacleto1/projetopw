from django.shortcuts import render

from .models import Post

from .forms import Postform

# Create your views here.

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'portfolio/home.html')

def about_me_view(request):
	return render(request, 'portfolio/aboutme.html')

def projects_view(request):
	return render(request, 'portfolio/projects.html')

def wp_view(request):
	return render(request, 'portfolio/wp.html')

def blog_view(request):
	blog_form = Postform(request.POST or None)
	if blog_form.is_valid():
		blog_form.save() 

	context = {'posts':sorted(Post.objects.all(), key=lambda post: post.data, reverse=True), 'form': blog_form}

	return render(request, "portfolio/blog.html" ,context)




def atw_view(request):
	return render(request, 'portfolio/atw.html')

def more_view(request):
	return render(request, 'portfolio/more.html')

def contact_view(request):
	return render(request, 'portfolio/contact.html')



