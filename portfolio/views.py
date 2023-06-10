from django.shortcuts import render

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
	return render(request, 'portfolio/blog.html')

def atw_view(request):
	return render(request, 'portfolio/atw.html')

def more_view(request):
	return render(request, 'portfolio/more.html')

def contact_view(request):
	return render(request, 'portfolio/contact.html')


