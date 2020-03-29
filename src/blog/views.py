from django.shortcuts import render

posts = [
    {
        'title':'التدوينه الاولى',
        'content':'هذا نص تجريبى خاص بالتدوينه الاولى',
        'author':'Mohamed ghalab',
        'date_posted':'29-3-2020'
    },
    {
        'title':'التدوينه الثانيه',
        'content':'هذا نص تجريبى خاص بالتدوينه الثانيه',
        'author':'Mohamed ghalab',
        'date_posted':'29-3-2020'
    },
    {
        'title':'التدوينه الثالثه',
        'content':'هذا نص تجريبى خاص بالتدوينه الثالثه',
        'author':'Mohamed ghalab',
        'date_posted':'29-3-2020'
    },
    {
        'title':'التدوينه الرابعه',
        'content':'هذا نص تجريبى خاص بالتدوينه الرابعه',
        'author':'Mohamed ghalab',
        'date_posted':'29-3-2020'
    }
]

def home(request):
    context = {
        'title':'الصفحة الرئيسيه',
        'posts':posts,
    }
    return render(request,'blog/index.html',context)

def about(request):
    return render(request, 'blog/about.html')