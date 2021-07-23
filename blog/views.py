from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post


# Create your views here.

def index(request):
    latest_posts = Post.objects.order_by('-date_posted')
    context = {
        'posts': latest_posts,
    }
    return render(request, 'blog/index.html', context) 

def about(request):
    return render(request, 'blog/about.html') 

def createPost(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST['title'])
        print(request.POST['content'])
    return render(request, 'blog/createpost.html') 

def details(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog/details.html', {'post': post })
