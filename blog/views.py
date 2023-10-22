# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import BlogPost, Comment
from .forms import CommentForm  # You'll create this form in the next step

# Create your views here.
def blog_post_list(request):
    blog_posts = BlogPost.objects.all().order_by('-pub_date')
    
    paginator = Paginator(blog_posts, 10)
    
    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        blog_posts = paginator.page(1)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)  
    return render(request, 'blog/blog_post_list.html', {'blog_posts': blog_posts})


def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    comments = blog_post.comments.all()
    
    # Retrieve the previous blog post based on publication date
    previous_blog_post = BlogPost.objects.filter(pub_date__lt=blog_post.pub_date).order_by('-pub_date').first()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = blog_post
            comment.save()
            return redirect('blog:blog_post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_post_detail.html', {
        'blog_post': blog_post,
        'comments': comments,
        'form': form,
        'previous_blog_post': previous_blog_post,  # Include the previous_blog_post in the context
    })
    
def comment_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'blog/comment_form.html', {'comment': comment})

def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('blog:comment_view', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:blog_post_detail', pk=comment.blog_post.pk)

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:blog_post_detail', pk=comment.blog_post.pk)

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:blog_post_detail', pk=comment.blog_post.pk)

def blog_post_new(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog:blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_post_edit.html', {'form': form})

def blog_post_edit(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog:blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/blog_post_edit.html', {'form': form})

def blog_post_delete(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    blog_post.delete()
    return redirect('blog:blog_post_list')

def blog_post_approve(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    blog_post.approve()
    return redirect('blog:blog_post_detail', pk=blog_post.pk)





















