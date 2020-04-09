from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم', max_length=30, help_text='اسم المستخدم يجب الا يحتوى على مسافات')
    email = forms.EmailField(label='البريد الالكترونى')
    first_name = forms.CharField(label='الاسم الاول', max_length=30)
    last_name = forms.CharField(label='الاسم الاخير', max_length=30)
    password1 = forms.CharField(label='كلمة المرور',min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(label='كرر كلمة المرور',min_length=8, widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')


    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلوة المرور غير متطابقه')
        return cd['password2']

    def clean_username(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')