from django.shortcuts import render, redirect
from .models import Post


def home(request):
    posts = Post.objects.filter(
        is_published=True
    ).order_by('-published_at')

    return render(request, 'main/home.html', {
        'posts': posts
    })


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if title and content and len(title) <= 2048:
            Post.objects.create(
                title=title,
                content=content
            )
            return redirect('home')

    return render(request, 'main/add_post.html')