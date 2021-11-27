from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm

from .models import Blog


def blog(request):
    """ A view to show all blogs """

    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def add_blog(request):
    """ Add a blog to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('home'))
        else:
            messages.error(request, (
                'Failed to add blog. '
                'Please ensure the form is valid.')
            )
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a Blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog')
            return redirect(reverse('blog'))
        else:
            messages.error(request, (
                'Failed to add blog. '
                'Please ensure the form is valid.')
            )
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.subject}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a Blog from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted!')
    return redirect(reverse('blog'))
