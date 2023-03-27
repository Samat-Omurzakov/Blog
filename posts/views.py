from django.shortcuts import render, redirect
from posts.forms import PostCreateForm
from posts.models import Post


# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        context = {
            'post': post,
            'comments': post.comment_set.all()
        }
        return render(request, 'posts/detail.html', context=context)


def post_create_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=context)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rating=form.cleaned_data.get('rating'),
                image=form.cleaned_data.get('image')
            )
            return redirect('/posts/')
        return render(request, 'posts/create.html', context={
            'form': form
        })