from django.shortcuts import render

from .models import Post

from .forms import Postform

from django .http import HttpResponseRedirect

from django.urls import reverse

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

	return render(request, "portfolio/blog.html" , context)


def delete_blog_post(request , id_post):
	Post.objects.get(id=id_post).delete()

	return HttpResponseRedirect(reverse(('portfolio:blog')))

def like_post(request, id_post):
    likesNoPost = Post.objects.get(id=id_post).like
    likesNoPost += 1
    Post.objects.filter(id=id_post).update(like=likesNoPost)
    
    return HttpResponseRedirect(reverse('portfolio:blog'))


def deslike_post(request, idP):
    deslikesNoPost = Post.objects.get(id=idP).deslike
    deslikesNoPost += 1
    Post.objects.filter(id=idP).update(deslike=deslikesNoPost)
    
    return HttpResponseRedirect(reverse('portfolio:blog'))


def atw_view(request):
	return render(request, 'portfolio/atw.html')

def more_view(request):
	return render(request, 'portfolio/more.html')

def contact_view(request):
	return render(request, 'portfolio/contact.html')



