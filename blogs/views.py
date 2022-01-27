from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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


@login_required()
def create_blog(request):
    print('ACCESS BEGINS')
    # if not request.user.is_authenticated:
    #     messages.error(request, 'You must be registered to be able to post a blog')
    #     return redirect(reverse('home'))

    if request.method == 'POST':  
        print('POST BEGINS')  
        form = BlogForm(request.POST, request.FILES)
        print('FORM AS BEEN FILLED, AND SAVED')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auther = request.user
            instance.save()
            messages.success(request, f'Your blog has been sent for consideration')


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


def requested_blogs(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access/permission to this page')
        return redirect(reverse('home'))

    blogs = Blog.objects.filter(publish=False)

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/requested_blogs.html', context)