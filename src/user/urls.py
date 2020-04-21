from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/',views.profile_update,name='profile_update'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
