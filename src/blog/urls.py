from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_view.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/',views.detail, name='detail'),
] 