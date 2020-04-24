from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_view.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/',views.detail, name='detail'),
    path('new_post/', views.PostCreatView.as_view(), name='new_post'),
    path('detail/<slug:pk>update/',views.PostUpdateView.as_view(), name='post_update'),
] 