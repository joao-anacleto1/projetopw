from django.shortcuts import render , redirect

from .models import Post

from .forms import Postform

from django .http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

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


def loginU(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('portfolio:home')
        
    return render(request, 'portfolio/login.html')



def logoutU(request):
    logout(request)
    return redirect('portfolio:home')


def registo(request):
    return render(request, "portfolio/register.html")


def registerU(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

    User.objects.create_user(name, email, password)
    return render(request, 'portfolio/login.html')
