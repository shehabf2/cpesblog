from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import	*
from .forms import *

# Create your views here.

def posts(request):
	
	posts = Post.objects.all()

	return render(request, 'posts.html', {'posts': posts})

def post_detail(request, pk):

	post = Post.objects.get(pk=pk)

	return render(request, 'post_detail.html', {'post':post})

def new_post(request):
	print("new post method")
	#form = PostForm()
	#return render(request, 'new_post.html', {'form':form})
	if request.method == 'POST':
		form =PostForm(request.POST)
		if form.is_valid():
			print('pass 2nd if')
			post = form.save()
			#post.author = Author.objects.get(name='arwa')
			post.publish_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		print("else")
		form = PostForm()
	return render(request, 'new_post.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = Author.objects.get(name='arwa')
			post.publish_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_edit.html', {'form': form})
