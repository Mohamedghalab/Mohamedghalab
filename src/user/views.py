from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'تهانينا تم التسجيل بنجاح ل {username}')
            return redirect('home')

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
            return redirect('home')
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