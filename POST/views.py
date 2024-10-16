from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #to prevent accessing a page without being authenticated or logged in

#import model object
from .models import Post

#import forms
from . import forms


def post_list(request):
	Posts = Post.objects.all()
	return render(request, "POSTS/post_list.html",{
		'Posts':Posts
		})


def post_page(request, slug):
	specificPost = Post.objects.get(slug=slug)
	return render(request, "POSTS/post_page.html",{
		"specificPost":specificPost
		})





@login_required(login_url='/users/login/')
def post_new(request):
	if request.method == "POST":
		form = forms.createPost(request.POST, request.FILES)
		if form.is_valid():
			# form.save()
			form_author = form.save(commit=False)
			form_author.author = request.user
			form_author.save()
			form.save()
			return redirect('POST:list')
	else:
		form = forms.createPost()

	return render(request, 'POSTS/post_new.html',{
		"form":form
		})


