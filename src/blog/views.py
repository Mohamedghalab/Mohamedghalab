from django.shortcuts import render ,get_object_or_404
from .models import Post, Comment
from .forms import NewComment
from django.views.generic import ListView

def home(request):
    posts=Post.objects.all()
    context = {
        'title':'الصفحة الرئيسيه',
        'posts':posts,
    }
    return render(request,'blog/index.html',context)

class Post_view(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html')


def detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = post.comments.filter(active=True)
    #check befor save comments
    if request.method =="POST":
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()

    context = {
        'title':post,
        'post':post,
        'comments':comments,
        'comment_form':comment_form,
    }

    return render(request,'blog/detail.html',context)