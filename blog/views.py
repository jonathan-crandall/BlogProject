from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Blog, Comments
from django.urls import reverse


def index(request):
    latest_posts_list = Blog.objects.order_by('-posted')[:3]
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'blog/index.html', context)


def techtips(request):
    context = {'time': timezone.now()}
    return render(request, 'blog/techtips.html', context)


def about(request):
    context = {'time': timezone.now()}
    return render(request, 'blog/about.html', context)


def archives(request):
    posts_list = Blog.objects.order_by('-posted')
    context = {'posts_list': posts_list}
    return render(request, 'blog/archive.html', context)


def entry(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/entry.html', {'blog': blog})


def comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        commenter = request.POST['commenter']
        email = request.POST['email']
        contents = request.POST['comment_content']
        posted = timezone.now()
        newComment = Comments(blog_id=blog_id, commenter=commenter, email=email, content=contents, posted=posted)
        newComment.save()
    except (KeyError, Comments.DoesNotExist):
        pass
        # something might go here
    return HttpResponseRedirect(reverse('blog:entry', args=(blog.id,)))
