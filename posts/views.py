from django.shortcuts import render
from posts.models import post
# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    context = {"gender":"female"}
    return render(request,'posts/list.html',context)
