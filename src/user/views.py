from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            #username=form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(request, f'تهانينا تم التسجيل بنجاح ل {new_user}')
            return redirect('login')

    else:
        form = UserCreationForm()
    context = {
        'title':'التسجيل',
        'form':form,
    }
    return render(request,'user/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(request, f' حدث خطأ فى تسجيل الدخول') 
    else:
        form = LoginForm()
    return render(request,'user/login.html',{
        'title':'تسجيل الدخول',
        'form':form
    })

def logout_user(request):
    logout(request)
    return render(request,'user/logout.html',{
        'title':'تسجيل الخروج',

    })


@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list,20)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request,'user/profile.html',{
        'title':'الملف الشخصى',
        'posts':posts,
        'post_list':post_list,
        'page':page

    })

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'تم تعديل الملف الشخصى بنجاخ')
            return redirect('profile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'title':'تعديل الصفحة الشخصيه',
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'user/profile_update.html',context)