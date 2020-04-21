from django.shortcuts import render ,get_object_or_404
from .models import Post, Comment
from .forms import NewComment, PostCreateForm
from django.views.generic import ListView, CreateView

def home(request):
    posts = Post.objects.all()
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


class PostCreatView(CreateView):
    model = Post
    #fields = ['title','content']
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
