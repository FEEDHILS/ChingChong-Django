from django.shortcuts import render, redirect
from .forms import PostsCreationForm

# Create your views here.
def postCreate(req):
    if req.method == 'POST':
        print(req.POST)
        new_Post = PostsCreationForm(req.POST)
        if new_Post.is_valid():
            new_post = new_Post.save(commit=False)
            new_post.sender = req.user
            new_post.save()

        new_Post.save()

    return render(req, "book.html")