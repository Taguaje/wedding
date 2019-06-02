from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('confirm_invite/', views.confirm_invite, name='confirm_invite'),
    path('confirm_transfer/', views.confirm_transfer, name='confirm_transfer'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
    path('set_email/', views.set_email, name='set_email'),
    path('menu/', views.menu, name='menu'),
    path('save_menu/', views.save_menu, name='save_menu'),
    path('view_menu/', views.view_menu, name='view_menu'),
    path('new_guest/', views.new_guest, name='new_guest')
]
