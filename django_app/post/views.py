from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)


def post_delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post:post_list')



def post_modify(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.save()

    return render(request, 'post_modify.html')

def post_create(request):
    user=User.objects.first()
    comment=request.POST['comment']
    Post.objects.create(
        author=user,
        comment=comment,
    )
    return render(request, 'post_create.html')
