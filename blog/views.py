from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import Post

# Create your views here.

def index(request):
    posts = get_list_or_404(Post)[:3]
    context ={
        "posts":posts
}
    return render(request,"blog/index.html",context)

def about(request):
    return render(request,"blog/about.html")

def locations(request):
    return render(request,"blog/locations.html")

def contact(request):
    return render(request,"blog/contact.html")

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context = {
        "post":post
}
    return render(request,"blog/detail.html",context)
