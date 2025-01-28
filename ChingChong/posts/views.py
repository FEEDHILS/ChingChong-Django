from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from main.models import Restaurant
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied

# Create your views here.
@login_required(login_url="login")
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

def postAll(req):
    ctx = dict()
    ctx['posts'] = Post.objects.filter(publish=True)
    return render(req, "posts/AllPosts.html", ctx)

@login_required(login_url="login")
def postMine(req):
    ctx = dict()
    ctx['posts'] = Post.objects.filter(sender=req.user)
    return render(req, "posts/MyPosts.html", ctx)


@login_required(login_url="login")
def postEdit(req, id):
    post = get_object_or_404(Post, pk=id)
    new_Post = PostsCreationForm(instance=post)
    # Проверка на то, является ли отправщиком текущий пользователь, или он админ
    if (req.user != post.sender) and not (req.user.has_perm('posts.change_post')):
        raise PermissionDenied("You cant edit other's posts")
    # Похожая проверка, но теперь учитывается что пост опубликован
    if post.publish and not (req.user.has_perm('posts.change_post')):
        raise PermissionDenied("You cant edit already published post")

    if req.method == 'POST':
        data = req.POST.copy()
        if data['restaurant'] == '0':
            data['restaurant'] = None
        
        data['sender'] = post.sender
        new_Post = PostsCreationForm(data=data, instance=post)
        if new_Post.is_valid():
            new_Post.save()
            PostsCreationForm.add_error(new_Post, None, "Your post has been edited")
            return redirect("profile")

    return render(req, "posts/Editbook.html", {"form": new_Post, "cities": Restaurant.objects.all()})