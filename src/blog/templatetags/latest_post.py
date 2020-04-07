from django import template
from blog.models import Post, Comment

register = template.Library()

@register.inclusion_tag('blog/latest_post.html')
def latest_post():
    posts = Post.objects.all()[:5]
    context = {
        'l_posts':posts
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')
def latest_comment():
    comment = Comment.objects.filter(active=True)[:5]
    context={
        'l_comments':comment
    }
    return context