from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('confirm_invite/', views.confirm_invite, name='confirm_invite'),
    path('confirm_transfer/', views.confirm_transfer, name='confirm_transfer'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar')
]
