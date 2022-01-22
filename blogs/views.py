from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


from .models import Blog
from .forms import BlogForm, PublishBlogForm


def view_blogs(request):
    # blogs = Blog.objects.all()

    blogs = Blog.objects.filter(publish=True)

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)


def read_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    # ADMIN CAN DECIDE WHETHER A BLOG SHOULD BE PUBLISHED; CAN NOT DELETE THE BLOG FROM HERE
    if request.method == 'POST': 
        form = PublishBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog {blog.name} will be published')
            return redirect(reverse('view_blogs'))
        else:
            messages.error(request, 'Blog {blog.name} will not be published')
    else:
        form = PublishBlogForm(instance=blog)

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blogs/read_blog.html', context)


def create_blog(request):
    if request.method == 'POST':    
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auther = request.user
            instance.save()
            messages.error(request, 'Your {blog.name} blog has been sent for consideration')

            return redirect(reverse('view_blogs'))
    else:   
        form = BlogForm()

    context = {
        'form': form
    }


    return render(request, 'blogs/create_blog.html', context)


def reject_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    messages.error(request, 'Blog has been deleted from teh database')

    return redirect(reverse('view_blogs'))