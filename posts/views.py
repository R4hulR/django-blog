from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'index.html',{'posts':posts})
def post(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'post.html',{'post':post})