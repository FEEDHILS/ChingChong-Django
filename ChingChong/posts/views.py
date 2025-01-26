from django.shortcuts import render, redirect
from .forms import PostsCreationForm
from main.models import Restaurant

# Create your views here.
def postCreate(req):
    new_Post = PostsCreationForm()
    if req.method == 'POST':
        data = req.POST.copy()

        data['sender'] = req.user
        if data['restaurant'] == '0':
            data['restaurant'] = None
        
        new_Post = PostsCreationForm(data)
        if new_Post.is_valid():
            new_Post.save()
            PostsCreationForm.add_error(new_Post, None, "Your post has been sent for moderation")

    return render(req, "posts/book.html", {"form": new_Post, "cities": Restaurant.objects.all()})